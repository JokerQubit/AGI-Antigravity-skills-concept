"""
Shared fixtures, configuration, and helper utilities for agi-antigravity-core tests.
"""
import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# Base paths
TESTS_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = TESTS_DIR.parent
WORKSPACE_ROOT = PLUGIN_ROOT.parent

# Approved Standard Registries
APPROVED_CORTEX_TOOLS: Set[str] = {
    "run_command",
    "view_file",
    "replace_file_content",
    "write_to_file",
    "list_dir",
    "grep_search",
    "find_by_name",
    "search_web",
    "read_url_content",
    "generate_image",
    "notebook_edit",
    "schedule",
    "manage_task",
    "send_message",
    "ask_permission",
    "ask_question",
    "invoke_subagent",
    "finish",
}

APPROVED_MCP_TOOLS: Set[str] = {
    # Chrome DevTools MCP tools
    "list_pages",
    "select_page",
    "new_page",
    "navigate_page",
    "close_page",
    "take_snapshot",
    "click",
    "fill",
    "hover",
    "press_key",
    "lighthouse_audit",
    "take_memory_snapshot",
    "performance_start_trace",
    "performance_stop_trace",
    "performance_analyze_insight",
    "list_network_requests",
    "list_console_messages",
    "evaluate_script",
    # Puppeteer MCP tools
    "puppeteer_navigate",
    "puppeteer_screenshot",
    "puppeteer_click",
    "puppeteer_fill",
    "puppeteer_hover",
    "puppeteer_evaluate",
}

ALL_APPROVED_TOOLS: Set[str] = APPROVED_CORTEX_TOOLS | APPROVED_MCP_TOOLS

# Forbidden placeholder patterns
FORBIDDEN_PLACEHOLDER_PATTERNS: List[Tuple[str, str]] = [
    (r"//\s*TODO\b", "C-style // TODO comment"),
    (r"/\*\s*TODO\b", "C-style /* TODO */ comment"),
    (r"#\s*TODO\b", "Python-style # TODO comment"),
    (r"\bTODO:\b", "Explicit TODO: label"),
    (r"\bFIXME:\b", "Explicit FIXME: label"),
    (r"\bpass\s*#\s*placeholder\b", "pass # placeholder statement"),
    (r"\bpass\s*#\s*TODO\b", "pass # TODO statement"),
    (r"\braise\s+NotImplementedError\b", "raise NotImplementedError stub"),
    (r"\bsynthetic_mock_array\b", "synthetic_mock_array placeholder"),
]


def parse_yaml_frontmatter(content: str) -> Tuple[Optional[Dict[str, str]], str]:
    """
    Parses simple YAML frontmatter delimited by --- at start of markdown.
    Returns (frontmatter_dict, markdown_body).
    """
    if not content.startswith("---"):
        return None, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content

    raw_yaml = parts[1].strip()
    body = parts[2].strip()

    frontmatter: Dict[str, str] = {}
    current_key: Optional[str] = None
    current_val_lines: List[str] = []

    for line in raw_yaml.splitlines():
        line_stripped = line.strip()
        if not line_stripped or line_stripped.startswith("#"):
            continue

        key_match = re.match(r"^([a-zA-Z0-9_-]+)\s*:\s*(.*)$", line)
        if key_match:
            if current_key is not None:
                frontmatter[current_key] = " ".join(current_val_lines).strip()
            current_key = key_match.group(1)
            rest = key_match.group(2).strip()
            if rest in (">-", ">", "|", "|-"):
                current_val_lines = []
            elif rest.startswith('"') and rest.endswith('"') and len(rest) >= 2:
                current_val_lines = [rest[1:-1]]
            elif rest.startswith("'") and rest.endswith("'") and len(rest) >= 2:
                current_val_lines = [rest[1:-1]]
            else:
                current_val_lines = [rest]
        else:
            if current_key is not None:
                current_val_lines.append(line_stripped)

    if current_key is not None:
        frontmatter[current_key] = " ".join(current_val_lines).strip()

    return frontmatter, body
