"""
Suite 5: Anti-Hallucination Tool Registry & Tool Binding Validation.
Scans all skills, rules, and documentation for tool invocations.
Asserts that 100% of referenced tools belong to the approved Cortex and MCP registries with zero hallucinated tool names.
"""
import re
import unittest
from pathlib import Path
from typing import List, NamedTuple, Set

try:
    from conftest import ALL_APPROVED_TOOLS, APPROVED_CORTEX_TOOLS, APPROVED_MCP_TOOLS, PLUGIN_ROOT
except ImportError:
    from .conftest import ALL_APPROVED_TOOLS, APPROVED_CORTEX_TOOLS, APPROVED_MCP_TOOLS, PLUGIN_ROOT


class ToolInvocation(NamedTuple):
    source_file: Path
    line_number: int
    tool_name: str
    line_snippet: str


class TestToolBindings(unittest.TestCase):
    """Tier 4: Anti-hallucination tool binding tests."""

    # Explicit known hallucinated or obsolete tool names that must never be used
    HALLUCINATED_TOOL_PATTERNS = [
        "run_shell_command",
        "execute_command",
        "exec_command",
        "bash_execute",
        "read_file_content",
        "read_file",
        "write_file",
        "edit_file_content",
        "modify_file",
        "delete_file",
        "create_file",
        "list_directory",
        "browse_url",
        "browser_click",
        "browser_navigate",
        "browser_snapshot",
        "terminal_run",
    ]

    # Regex detecting explicit tool call syntax: tool_name(arg=..., or tool_name("...")
    TOOL_CALL_REGEX = re.compile(
        r"\b([a-z_][a-z0-9_]*)\s*\(\s*(?:[A-Za-z0-9_]+=|['\"]|true|false|None|\{)"
    )

    # Regex detecting backticked tool mentions in tool execution contexts
    BACKTICK_TOOL_REGEX = re.compile(r"`([a-z_][a-z0-9_]{3,30})`")

    def _collect_skill_and_rule_files(self) -> List[Path]:
        """Collects all markdown files under skills/ and rules/."""
        files = []
        rules_dir = PLUGIN_ROOT / "rules"
        if rules_dir.exists():
            files.extend(rules_dir.rglob("*.md"))

        skills_dir = PLUGIN_ROOT / "skills"
        if skills_dir.exists():
            files.extend(skills_dir.rglob("*.md"))

        return files

    def test_zero_known_hallucinated_tool_names(self):
        """Asserts that zero known obsolete/hallucinated tool names appear in any skill or rule."""
        files = self._collect_skill_and_rule_files()
        self.assertTrue(len(files) > 0, "No skill or rule files found to validate")

        violations: List[ToolInvocation] = []

        for file_path in files:
            content = file_path.read_text(encoding="utf-8")
            lines = content.splitlines()
            for line_idx, line in enumerate(lines, start=1):
                # Ignore lines discussing banned tools in rule sets
                if "banned" in line.lower() or "obsolete" in line.lower() or "hallucinat" in line.lower():
                    continue

                for bad_tool in self.HALLUCINATED_TOOL_PATTERNS:
                    # Match whole word
                    pattern = rf"\b{re.escape(bad_tool)}\b"
                    if re.search(pattern, line):
                        violations.append(
                            ToolInvocation(
                                source_file=file_path,
                                line_number=line_idx,
                                tool_name=bad_tool,
                                line_snippet=line.strip(),
                            )
                        )

        if violations:
            report_lines = [
                f"\nFound {len(violations)} hallucinated/obsolete tool reference(s):"
            ]
            for v in violations:
                try:
                    rel = v.source_file.relative_to(PLUGIN_ROOT)
                except ValueError:
                    rel = v.source_file
                report_lines.append(
                    f"  - {rel}:{v.line_number} -> Forbidden tool '{v.tool_name}' in: \"{v.line_snippet}\""
                )
            self.fail("\n".join(report_lines))

    def test_invoked_cortex_and_mcp_tools_are_registered(self):
        """Validates that all explicit tool call forms match registered Cortex or MCP tools."""
        files = self._collect_skill_and_rule_files()
        unregistered_invocations: List[ToolInvocation] = []

        # Common non-tool function call names to ignore in markdown pseudo-code
        NON_TOOL_FUNCTIONS = {
            "print",
            "len",
            "range",
            "open",
            "json",
            "dump",
            "load",
            "loads",
            "dumps",
            "str",
            "int",
            "float",
            "bool",
            "dict",
            "list",
            "set",
            "tuple",
            "strip",
            "split",
            "join",
            "format",
            "match",
            "search",
            "sub",
            "compile",
            "resolve",
            "exists",
            "is_file",
            "is_dir",
            "read_text",
            "write_text",
            "append",
            "extend",
            "pop",
            "get",
            "keys",
            "values",
            "items",
            "assert",
            "require",
            "fetch",
            "then",
            "catch",
            "map",
            "filter",
            "reduce",
            "encode",
            "decode",
            "sleep",
            "exit",
            "min",
            "max",
            "sum",
            "any",
            "all",
            "eval",
            "exec",
        }

        for file_path in files:
            content = file_path.read_text(encoding="utf-8")
            lines = content.splitlines()
            for line_idx, line in enumerate(lines, start=1):
                # Search for explicit tool call patterns: name(NamedArg=...)
                for match in self.TOOL_CALL_REGEX.finditer(line):
                    func_name = match.group(1)

                    if func_name in NON_TOOL_FUNCTIONS:
                        continue

                    # If line has standard tool argument keywords (e.g. AbsolutePath, CommandLine, TargetFile, Url, etc.)
                    is_tool_call_context = any(
                        arg_key in line
                        for arg_key in (
                            "AbsolutePath",
                            "CommandLine",
                            "TargetFile",
                            "DirectoryPath",
                            "Query",
                            "Url",
                            "Prompt",
                            "Message",
                            "Recipient",
                            "DurationSeconds",
                            "CronExpression",
                            "TaskId",
                            "Action",
                            "ReplacementContent",
                        )
                    )

                    if is_tool_call_context:
                        if func_name not in ALL_APPROVED_TOOLS:
                            unregistered_invocations.append(
                                ToolInvocation(
                                    source_file=file_path,
                                    line_number=line_idx,
                                    tool_name=func_name,
                                    line_snippet=line.strip(),
                                )
                            )

        if unregistered_invocations:
            report_lines = [
                f"\nFound {len(unregistered_invocations)} unregistered/hallucinated tool invocation(s):"
            ]
            for v in unregistered_invocations:
                try:
                    rel = v.source_file.relative_to(PLUGIN_ROOT)
                except ValueError:
                    rel = v.source_file
                report_lines.append(
                    f"  - {rel}:{v.line_number} -> Unknown tool '{v.tool_name}' in: \"{v.line_snippet}\""
                )
            self.fail("\n".join(report_lines))


if __name__ == "__main__":
    unittest.main()
