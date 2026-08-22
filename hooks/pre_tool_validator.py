#!/usr/bin/env python3
"""
Pre-Tool Validator Hook for agi-antigravity-core.

Validates incoming tool calls before execution in the Antigravity agent loop.
Enforces security constraints, blocks destructive commands, sanitizes file paths,
and detects deprecated tool names.
"""

import json
import re
import sys
from typing import Any, Dict, List, Tuple

# Patterns identifying dangerous or destructive shell commands
DESTRUCTIVE_COMMAND_PATTERNS: List[re.Pattern] = [
    # 1. POSIX recursive root/system directory deletions (combined flags, split flags, --no-preserve-root, critical subdirs, home)
    re.compile(
        r"\brm\b(?=.*?(?:-[a-zA-Z0-9-]*[rR][a-zA-Z0-9-]*|--recursive))(?=.*?(?:(?:^|\s|['\"])/(?:etc|usr|var|bin|sbin|boot|sys|dev|lib|lib64|root|home|proc|opt)\b|(?:^|\s|['\"])/(?:\s|$|\*|['\"])|(?:^|\s|['\"])\~(?:\s|$|/|['\"])|--no-preserve-root)).*",
        re.IGNORECASE,
    ),
    re.compile(r"\brm\s+.*--no-preserve-root", re.IGNORECASE),

    # 2. Windows cmd.exe destructive file deletions (del, erase with multi-switches)
    re.compile(
        r"\b(?:del|erase)\b.*?(?:[a-zA-Z]:[\\/]+|%systemroot%|%windir%)(?:windows|system32|boot|recovery|program files|users|\*|\*\.\*)",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:del|erase)\b(?=.*?(?:/[fFqQsS]|-[fFqQsS])).*?(?:[a-zA-Z]:[\\/]+|/(?:\s|$|\*))",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:del|erase)\s+(?:/[a-zA-Z0-9:]+\s+)*[a-zA-Z]:[\\/]*(?:windows|system32)?(?:\s|$|\*|\.\*|[\"'])",
        re.IGNORECASE,
    ),

    # 3. Windows cmd.exe directory removals (rd, rmdir targeting root or system dirs)
    re.compile(
        r"\b(?:rd|rmdir)\b.*?(?:[a-zA-Z]:[\\/]*)(?:windows|system32|boot|recovery|program files|users|\s*$|\s+/[a-zA-Z]|\s*[\"'])",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:rd|rmdir)\s+(?:/[a-zA-Z0-9:]+\s+)*[a-zA-Z]:[\\/]*(?:\s|$|\*|[\"'])",
        re.IGNORECASE,
    ),
    re.compile(
        r"\b(?:rd|rmdir)\b.*?(?:(?:^|\s|['\"])/(?:etc|usr|var|bin|sbin|boot|sys|dev|lib|lib64|root|home|proc|opt)\b|(?:^|\s|['\"])/(?:\s|$|\*|['\"]))",
        re.IGNORECASE,
    ),

    # 4. PowerShell destructive removals (Remove-Item, ri, rmdir, del, erase with -Recurse & -Force)
    re.compile(
        r"\b(?:Remove-Item|ri|rmdir|del|erase)\b(?=.*?(?:-Recurse|-r\b))(?=.*?(?:-Force|-fo\b)).*?(?:[a-zA-Z]:[\\/]*|/(?:\s|$|\*)|~)",
        re.IGNORECASE,
    ),

    # 5. Disk format and raw block device manipulation
    re.compile(r"\bformat\s+[a-zA-Z]:", re.IGNORECASE),
    re.compile(r"\bmkfs(?:\.\w+)?\s+", re.IGNORECASE),
    re.compile(
        r"\bdd\s+if=.*?\bof=(?:/dev/[sh]d[a-z0-9]|/dev/nvme\d+n\d+|\\\\\\.\\PhysicalDrive\d+)",
        re.IGNORECASE,
    ),
    re.compile(r"(?:>|>>)\s*/dev/(?:[sh]d[a-z0-9]|nvme\d+n\d+)", re.IGNORECASE),

    # 6. Fork bombs (with arbitrary whitespace)
    re.compile(r":\s*\(\s*\)\s*\{\s*:\s*\|\s*:\s*&\s*\}\s*;\s*:", re.IGNORECASE),

    # 7. System shutdown, reboot, halt
    re.compile(r"\bshutdown\s+[-/][a-zA-Z0-9\s/-]+", re.IGNORECASE),
    re.compile(r"\binit\s+[06]\b", re.IGNORECASE),
    re.compile(r"\b(?:poweroff|reboot|halt)\b", re.IGNORECASE),

    # 8. Encoded / obfuscated command execution
    re.compile(r"\bpowershell(?:\.exe)?\s+.*-(?:enc|encodedcommand|e)\s+[A-Za-z0-9+/=]{10,}", re.IGNORECASE),
    re.compile(r"\bbase64\s+-(?:d|-decode)\s*\|\s*(?:ba)?sh\b", re.IGNORECASE),
]

# Deprecated or phantom tool names that should be blocked with corrective guidance
DEPRECATED_TOOL_MAPPINGS: Dict[str, str] = {
    "run_shell_command": "Use 'run_command' instead.",
    "browser": "Use authorized MCP tools (e.g. 'puppeteer_*') or 'search_web' instead.",
    "execute_script": "Use 'run_command' with appropriate interpreter instead.",
    "create_file": "Use 'write_to_file' instead.",
    "edit_file": "Use 'replace_file_content' instead.",
    "search_directory": "Use 'grep_search' or 'find_by_name' instead.",
    "list_directory": "Use 'list_dir' instead.",
}

PATH_KEYS = (
    "TargetPath",
    "TargetFile",
    "AbsolutePath",
    "SearchDirectory",
    "DirectoryPath",
    "SearchPath",
    "Cwd",
    "NotebookPath",
    "ImagePaths",
)


def is_destructive_command(cmd: str) -> Tuple[bool, str]:
    """Check if command matches known destructive patterns."""
    for pattern in DESTRUCTIVE_COMMAND_PATTERNS:
        match = pattern.search(cmd)
        if match:
            return True, match.group(0)
    return False, ""


def validate_path_safety(val: Any) -> Tuple[bool, str]:
    """Check for null bytes and malformed path injections."""
    if isinstance(val, str):
        if "\x00" in val:
            return False, "Null byte injection detected in path argument."
    elif isinstance(val, (list, tuple)):
        for item in val:
            if isinstance(item, str) and "\x00" in item:
                return False, "Null byte injection detected in path list element."
    return True, ""


def process_tool_validation(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Validate tool call and return Antigravity-compliant decision payload."""
    tool_call = payload.get("toolCall", {})
    if not isinstance(tool_call, dict):
        return {
            "decision": "allow",
            "reason": "Malformed or non-dict toolCall payload; permitting default execution."
        }

    tool_name = tool_call.get("name", "")
    if not isinstance(tool_name, str):
        tool_name = ""

    tool_args = tool_call.get("args", {})
    if not isinstance(tool_args, dict):
        tool_args = {}

    # 1. Check for deprecated or phantom tool names
    if tool_name in DEPRECATED_TOOL_MAPPINGS:
        return {
            "decision": "deny",
            "reason": f"Deprecated tool '{tool_name}' blocked. {DEPRECATED_TOOL_MAPPINGS[tool_name]}"
        }

    # 2. Check for destructive shell commands
    if tool_name == "run_command":
        cmd_line = tool_args.get("CommandLine", "")
        if isinstance(cmd_line, str):
            is_bad, matched = is_destructive_command(cmd_line)
            if is_bad:
                return {
                    "decision": "deny",
                    "reason": f"Destructive command pattern detected: '{matched}'. Execution blocked by pre-tool safety firewall."
                }

    # 3. Check for path safety across known filesystem arguments
    for key in PATH_KEYS:
        if key in tool_args:
            is_safe, error_msg = validate_path_safety(tool_args[key])
            if not is_safe:
                return {
                    "decision": "deny",
                    "reason": f"Invalid path parameter '{key}': {error_msg}"
                }

    # 4. Tool call validated and permitted
    return {
        "decision": "allow",
        "reason": f"Tool call '{tool_name}' verified safe by pre-tool validator."
    }


def main() -> None:
    """Main hook entry point reading JSON from stdin and writing JSON to stdout."""
    raw_input = sys.stdin.read().strip()
    if not raw_input:
        # If no stdin was provided, allow default execution gracefully
        output = {"decision": "allow", "reason": "No input payload received; default allow."}
        sys.stdout.write(json.dumps(output))
        sys.stdout.flush()
        return

    try:
        payload = json.loads(raw_input)
        if not isinstance(payload, dict):
            payload = {}
        result = process_tool_validation(payload)
    except Exception as exc:
        # Fail safe on malformed JSON or internal errors
        result = {
            "decision": "allow",
            "reason": f"Pre-tool validator error handling request: {exc}. Permitting execution."
        }

    sys.stdout.write(json.dumps(result))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
