"""
Suite 6: Lifecycle Hooks Contract & Execution Validation.
Executes hooks/*.py scripts with simulated JSON payloads on stdin, asserting correct stdout JSON schema,
decision logic, and error resilience under Antigravity 2.0 lifecycle specifications.
"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

try:
    from conftest import PLUGIN_ROOT
except ImportError:
    from .conftest import PLUGIN_ROOT


class TestHooksContract(unittest.TestCase):
    """Tier 4: Dynamic lifecycle hook contract tests."""

    @classmethod
    def setUpClass(cls):
        cls.hooks_dir = PLUGIN_ROOT / "hooks"
        cls.pre_tool_script = cls.hooks_dir / "pre_tool_validator.py"
        cls.post_tool_script = cls.hooks_dir / "post_tool_linter.py"
        cls.stop_script = cls.hooks_dir / "stop_gatekeeper.py"

    def _run_hook(self, script_path: Path, input_payload: dict, timeout_sec: int = 10) -> dict:
        """Helper to run a hook script via Python subprocess and parse stdout JSON."""
        input_json = json.dumps(input_payload)
        proc = subprocess.Popen(
            [sys.executable, str(script_path)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(PLUGIN_ROOT),
            text=True,
        )
        try:
            stdout_str, stderr_str = proc.communicate(input=input_json, timeout=timeout_sec)
        except subprocess.TimeoutExpired:
            proc.kill()
            self.fail(f"Hook script {script_path.name} timed out after {timeout_sec}s")

        self.assertEqual(
            proc.returncode,
            0,
            f"Hook script {script_path.name} failed with exit code {proc.returncode}.\nStderr: {stderr_str}",
        )

        stdout_trimmed = stdout_str.strip()
        self.assertTrue(
            len(stdout_trimmed) > 0,
            f"Hook script {script_path.name} produced empty stdout. Expected JSON.",
        )

        try:
            result = json.loads(stdout_trimmed)
        except json.JSONDecodeError as e:
            self.fail(
                f"Hook script {script_path.name} stdout is not valid JSON: '{stdout_trimmed}'. Error: {e}"
            )

        self.assertIsInstance(
            result, dict, f"Hook {script_path.name} stdout JSON must be an object"
        )
        return result

    def test_hook_scripts_exist_and_compile(self):
        """Validates that hook scripts exist and are syntactically valid Python."""
        self.assertTrue(
            self.hooks_dir.exists(), f"Hooks directory not found at {self.hooks_dir}"
        )

        for script in (self.pre_tool_script, self.post_tool_script, self.stop_script):
            with self.subTest(script=script.name):
                self.assertTrue(script.exists(), f"Hook script not found: {script}")
                content = script.read_text(encoding="utf-8")
                try:
                    compile(content, str(script), "exec")
                except SyntaxError as e:
                    self.fail(f"Syntax error in hook script {script.name}: {e}")

    def test_pre_tool_validator_safe_command(self):
        """Validates PreToolUse hook on standard safe command execution."""
        payload = {
            "conversationId": "test-conv-001",
            "stepIdx": 1,
            "toolCall": {
                "name": "run_command",
                "args": {"CommandLine": "python -m pytest tests/"},
            },
            "workspacePaths": [str(PLUGIN_ROOT)],
            "transcriptPath": str(PLUGIN_ROOT / "transcript.jsonl"),
            "artifactDirectoryPath": str(PLUGIN_ROOT / "artifacts"),
            "modelName": "auto",
        }
        res = self._run_hook(self.pre_tool_script, payload)
        self.assertIn("decision", res, "PreToolUse output must include 'decision'")
        self.assertIn(
            res["decision"],
            {"allow", "deny", "ask", "force_ask"},
            f"Invalid decision '{res.get('decision')}'. Must be allow/deny/ask/force_ask.",
        )
        self.assertEqual(res["decision"], "allow")

    def test_pre_tool_validator_dangerous_command_blocked(self):
        """Validates PreToolUse hook blocks or prompts on destructive / dangerous commands across POSIX, Windows, and PowerShell."""
        dangerous_commands = [
            # POSIX root, split flags, subdirectories, and home
            "rm -rf /",
            "rm -r -f /",
            "rm -f -r /",
            "rm -r -F /",
            "rm --no-preserve-root -rf /",
            "rm -rf /etc",
            "rm -rf /usr",
            "rm -rf /var",
            "rm -rf ~",
            # Windows multi-switch deletions and directory wipes
            r"del /f /s /q C:\Windows",
            r"del /s /q C:\Windows\System32",
            r"del /f /q c:\windows\system32",
            r"DEL /S /Q D:\WINDOWS",
            r"del /f /s C:\Windows",
            r"rd /s /q C:\Windows",
            "rmdir /s /q C:\\",
            "rd /s /q C:\\",
            # PowerShell deletions
            r"Remove-Item -Recurse -Force C:\Windows",
            "ri -r -fo C:\\",
            # Formatting and block devices
            "format C: /y",
            "format D: /fs:NTFS /q",
            "mkfs /dev/sda1",
            "dd if=/dev/zero of=/dev/sda",
            # Fork bombs (standard and spaced)
            ":(){ :|:& };:",
            ": ( ) { : | : & } ; :",
            # Shutdown and init states
            "shutdown /s",
            "shutdown /r",
            "shutdown /t 0 /s",
            "init 0",
            "init 6",
        ]
        for cmd in dangerous_commands:
            with self.subTest(cmd=cmd):
                payload = {
                    "conversationId": "test-conv-002",
                    "stepIdx": 2,
                    "toolCall": {
                        "name": "run_command",
                        "args": {"CommandLine": cmd},
                    },
                    "workspacePaths": [str(PLUGIN_ROOT)],
                }
                res = self._run_hook(self.pre_tool_script, payload)
                self.assertIn("decision", res)
                self.assertIn(
                    res["decision"],
                    {"deny", "ask", "force_ask"},
                    f"Dangerous command '{cmd}' was unexpectedly allowed without prompt/block",
                )
                self.assertIn(
                    "reason",
                    res,
                    "Blocked/prompted command should include explanation in 'reason'",
                )

    def test_pre_tool_validator_path_safety_list_arguments(self):
        """Validates PreToolUse hook blocks null-byte injections in list and string path arguments."""
        # List argument with null-byte injection
        list_payload = {
            "conversationId": "test-conv-list-001",
            "stepIdx": 1,
            "toolCall": {
                "name": "generate_image",
                "args": {
                    "Prompt": "generate diagram",
                    "ImageName": "arch_diagram",
                    "ImagePaths": ["d:/safe.png", "d:/bad\x00.png"],
                },
            },
            "workspacePaths": [str(PLUGIN_ROOT)],
        }
        res_list = self._run_hook(self.pre_tool_script, list_payload)
        self.assertEqual(res_list.get("decision"), "deny")
        self.assertIn("Null byte", res_list.get("reason", ""))

        # String argument with null-byte injection
        string_payload = {
            "conversationId": "test-conv-str-001",
            "stepIdx": 2,
            "toolCall": {
                "name": "notebook_edit",
                "args": {
                    "NotebookPath": "d:/safe\x00malicious.ipynb",
                    "Action": "list",
                },
            },
            "workspacePaths": [str(PLUGIN_ROOT)],
        }
        res_str = self._run_hook(self.pre_tool_script, string_payload)
        self.assertEqual(res_str.get("decision"), "deny")
        self.assertIn("Null byte", res_str.get("reason", ""))

    def test_pre_tool_validator_deprecated_tools_blocked(self):
        """Validates PreToolUse hook blocks deprecated tools with guidance."""
        deprecated_tools = ["run_shell_command", "browser", "create_file", "search_directory"]
        for tool in deprecated_tools:
            with self.subTest(tool=tool):
                payload = {
                    "conversationId": "test-conv-dep-001",
                    "stepIdx": 1,
                    "toolCall": {"name": tool, "args": {}},
                    "workspacePaths": [str(PLUGIN_ROOT)],
                }
                res = self._run_hook(self.pre_tool_script, payload)
                self.assertEqual(res.get("decision"), "deny")
                self.assertIn("reason", res)
                self.assertIn("instead", res["reason"].lower())

    def test_post_tool_linter_contract(self):
        """Validates PostToolUse hook returns valid empty object or lint recommendations."""
        payload = {
            "conversationId": "test-conv-003",
            "stepIdx": 3,
            "toolCall": {
                "name": "write_to_file",
                "args": {
                    "TargetFile": str(PLUGIN_ROOT / "temp_check.py"),
                    "CodeContent": "x = 1\n",
                },
            },
            "workspacePaths": [str(PLUGIN_ROOT)],
        }
        res = self._run_hook(self.post_tool_script, payload)
        self.assertIsInstance(res, dict)

    def test_stop_gatekeeper_contract(self):
        """Validates Stop hook input/output contract."""
        payload = {
            "conversationId": "test-conv-004",
            "executionNum": 1,
            "terminationReason": "model_stop",
            "fullyIdle": True,
            "workspacePaths": [str(PLUGIN_ROOT)],
        }
        res = self._run_hook(self.stop_script, payload)
        self.assertIsInstance(res, dict)
        if "decision" in res:
            self.assertIn(
                res["decision"],
                {"continue", "allow", "stop"},
                f"Unexpected Stop hook decision: {res['decision']}",
            )

    def test_hooks_resilience_on_empty_or_malformed_input(self):
        """Validates that hooks fail closed safely on malformed JSON without crashing."""
        for script in (self.pre_tool_script, self.post_tool_script, self.stop_script):
            with self.subTest(script=script.name):
                proc = subprocess.Popen(
                    [sys.executable, str(script)],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    cwd=str(PLUGIN_ROOT),
                    text=True,
                )
                stdout_str, stderr_str = proc.communicate(input="{invalid_json}", timeout=10)
                self.assertEqual(
                    proc.returncode,
                    0,
                    f"Hook {script.name} crashed on malformed input. Stderr: {stderr_str}",
                )
                try:
                    res = json.loads(stdout_str.strip())
                    self.assertIsInstance(res, dict)
                except Exception as e:
                    self.fail(f"Hook {script.name} did not return valid fallback JSON: {e}")


if __name__ == "__main__":
    unittest.main()
