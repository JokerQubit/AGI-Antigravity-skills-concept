"""
Adversarial Stress Test Suite for agi-antigravity-core Milestone 1 Deliverables.
Empirically stress-tests:
- hooks/pre_tool_validator.py
- hooks/post_tool_linter.py
- hooks/stop_gatekeeper.py
- plugin.json, mcp_config.json, hooks.json
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


class TestAdversarialHooksM1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hooks_dir = PLUGIN_ROOT / "hooks"
        cls.pre_tool_script = cls.hooks_dir / "pre_tool_validator.py"
        cls.post_tool_script = cls.hooks_dir / "post_tool_linter.py"
        cls.stop_script = cls.hooks_dir / "stop_gatekeeper.py"

    def _execute_hook_raw(self, script_path: Path, raw_stdin: str, timeout_sec: int = 5):
        """Helper to run a hook script with raw text on stdin."""
        proc = subprocess.Popen(
            [sys.executable, str(script_path)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=str(PLUGIN_ROOT),
            text=True,
        )
        try:
            stdout_str, stderr_str = proc.communicate(input=raw_stdin, timeout=timeout_sec)
        except subprocess.TimeoutExpired:
            proc.kill()
            self.fail(f"Hook script {script_path.name} timed out after {timeout_sec}s")

        return proc.returncode, stdout_str, stderr_str

    def _execute_hook_json(self, script_path: Path, payload: dict, timeout_sec: int = 5) -> dict:
        """Helper to run a hook with JSON payload and assert valid JSON response and returncode 0."""
        raw_stdin = json.dumps(payload)
        code, stdout_str, stderr_str = self._execute_hook_raw(script_path, raw_stdin, timeout_sec)
        self.assertEqual(code, 0, f"Hook {script_path.name} exited with non-zero code {code}. Stderr: {stderr_str}")
        self.assertTrue(len(stdout_str.strip()) > 0, f"Hook {script_path.name} produced empty stdout.")
        try:
            result = json.loads(stdout_str.strip())
        except Exception as e:
            self.fail(f"Hook {script_path.name} stdout is not valid JSON: {stdout_str.strip()}. Error: {e}")
        self.assertIsInstance(result, dict, f"Hook {script_path.name} stdout must parse into a dict.")
        return result

    # ==========================================
    # 1. PRE-TOOL VALIDATOR: DESTRUCTIVE COMMANDS
    # ==========================================
    def test_destructive_posix_commands_blocked(self):
        """Assert all POSIX destructive commands are blocked."""
        commands = [
            "rm -rf /",
            "rm -rf /*",
            "rm -r -f /",
            "rm -Rf /",
            "rm -r -F /",
            "rm -fr /",
            "rm -f -r /",
            "echo hello && rm -rf /",
            "pytest; rm -rf /",
            "mkfs /dev/sda1",
            "mkfs.ext4 /dev/nvme0n1",
            "dd if=/dev/zero of=/dev/sda",
            "dd if=/dev/urandom of=/dev/hda",
            "> /dev/sda",
            ":(){ :|:& };:",
            ": ( ) { : | : & } ; :",
            "init 0",
        ]
        for cmd in commands:
            with self.subTest(cmd=cmd):
                payload = {
                    "toolCall": {
                        "name": "run_command",
                        "args": {"CommandLine": cmd}
                    }
                }
                res = self._execute_hook_json(self.pre_tool_script, payload)
                self.assertEqual(
                    res.get("decision"), "deny",
                    f"Destructive command '{cmd}' was not blocked. Response: {res}"
                )

    def test_destructive_windows_commands_blocked(self):
        """Assert all Windows destructive commands are blocked."""
        commands = [
            r"del /f /s /q C:\Windows",
            r"del /s /q C:\Windows\System32",
            r"del /f /q c:\windows\system32",
            r"DEL /S /Q D:\WINDOWS",
            r"del /f /s C:\Windows",
            "format C:",
            "format D: /fs:NTFS /q",
            "shutdown /s",
            "shutdown /t 0 /s",
            "shutdown /s /t 0",
        ]
        for cmd in commands:
            with self.subTest(cmd=cmd):
                payload = {
                    "toolCall": {
                        "name": "run_command",
                        "args": {"CommandLine": cmd}
                    }
                }
                res = self._execute_hook_json(self.pre_tool_script, payload)
                self.assertEqual(
                    res.get("decision"), "deny",
                    f"Destructive Windows command '{cmd}' was not blocked. Response: {res}"
                )

    def test_safe_shell_commands_allowed(self):
        """Assert standard development shell commands are allowed."""
        safe_commands = [
            "python -m pytest tests/",
            "npm test",
            "git status",
            "git commit -m 'feat: update'",
            "echo 'hello world'",
            "cat package.json",
            "dir",
            "ls -la",
            "rmdir /s /q temp_build",
            "rm temp_file.txt",
            "cargo test --all",
            "flake8 agi-antigravity-core/",
        ]
        for cmd in safe_commands:
            with self.subTest(cmd=cmd):
                payload = {
                    "toolCall": {
                        "name": "run_command",
                        "args": {"CommandLine": cmd}
                    }
                }
                res = self._execute_hook_json(self.pre_tool_script, payload)
                self.assertEqual(
                    res.get("decision"), "allow",
                    f"Safe command '{cmd}' was unexpectedly blocked. Response: {res}"
                )

    # ==========================================
    # 2. PRE-TOOL VALIDATOR: DEPRECATED TOOLS
    # ==========================================
    def test_deprecated_tools_blocked(self):
        """Assert deprecated tool names are blocked with migration guidance."""
        deprecated = [
            "run_shell_command",
            "browser",
            "execute_script",
            "create_file",
            "edit_file",
            "search_directory",
            "list_directory",
        ]
        for tool in deprecated:
            with self.subTest(tool=tool):
                payload = {"toolCall": {"name": tool, "args": {}}}
                res = self._execute_hook_json(self.pre_tool_script, payload)
                self.assertEqual(res.get("decision"), "deny")
                self.assertIn("reason", res)
                self.assertIn("instead", res["reason"].lower())

    def test_valid_tools_allowed(self):
        """Assert all valid tools are allowed."""
        valid_tools = [
            "run_command",
            "read_url_content",
            "read_browser_page",
            "write_to_file",
            "replace_file_content",
            "grep_search",
            "find_by_name",
            "list_dir",
            "view_file",
            "send_message",
            "manage_task",
            "schedule",
            "generate_image",
            "notebook_edit",
        ]
        for tool in valid_tools:
            with self.subTest(tool=tool):
                payload = {"toolCall": {"name": tool, "args": {}}}
                res = self._execute_hook_json(self.pre_tool_script, payload)
                self.assertEqual(res.get("decision"), "allow")

    # ==========================================
    # 3. PRE-TOOL VALIDATOR: PATH SAFETY & NULL BYTES
    # ==========================================
    def test_null_byte_path_injections_blocked(self):
        """Assert null byte injection in any path parameter is blocked."""
        path_keys = [
            "TargetPath", "TargetFile", "AbsolutePath",
            "SearchDirectory", "DirectoryPath", "SearchPath", "Cwd"
        ]
        for key in path_keys:
            with self.subTest(key=key):
                payload = {
                    "toolCall": {
                        "name": "write_to_file",
                        "args": {key: f"valid_prefix/safe.py\x00malicious.sh"}
                    }
                }
                res = self._execute_hook_json(self.pre_tool_script, payload)
                self.assertEqual(res.get("decision"), "deny")
                self.assertIn("Null byte", res.get("reason", ""))

    # ==========================================
    # 4. PRE-TOOL VALIDATOR: ADVERSARIAL PAYLOADS & MALFORMATIONS
    # ==========================================
    def test_pre_tool_validator_malformed_inputs_never_crash(self):
        """Assert pre_tool_validator never crashes on malformed inputs."""
        malformed_inputs = [
            "",                                      # Empty stdin
            "   \n\t  \n  ",                        # Whitespace only
            "{invalid_json",                         # Truncated JSON
            "not json at all",                       # Plain text
            "null",                                  # JSON null
            "12345",                                 # JSON number
            "true",                                  # JSON boolean
            '["a", "b", "c"]',                       # JSON array
            '{"toolCall": null}',                    # Null toolCall
            '{"toolCall": {"name": null}}',          # Null tool name
            '{"toolCall": {"name": "run_command", "args": null}}', # Null args
            '{"toolCall": {"name": "run_command", "args": {"CommandLine": null}}}', # Null CommandLine
            '{"toolCall": {"name": "run_command", "args": {"CommandLine": 12345}}}', # Integer CommandLine
            '{"toolCall": {"name": "write_to_file", "args": {"TargetFile": ["list"]}}}', # List TargetFile
            '{"toolCall": {"name": "write_to_file", "args": {"TargetFile": 9999}}}', # Integer TargetFile
            json.dumps({"toolCall": {"name": "run_command", "args": {"CommandLine": "x" * 100000}}}), # 100KB command
        ]
        for inp in malformed_inputs:
            with self.subTest(input_sample=inp[:30] if len(inp) > 30 else inp):
                code, stdout, stderr = self._execute_hook_raw(self.pre_tool_script, inp)
                self.assertEqual(code, 0, f"Hook crashed with code {code} on input: {inp[:40]}. Stderr: {stderr}")
                try:
                    res = json.loads(stdout.strip())
                    self.assertIsInstance(res, dict)
                    self.assertIn("decision", res)
                except Exception as e:
                    self.fail(f"Hook did not return valid JSON on malformed input. Stdout: {stdout}. Error: {e}")

    # ==========================================
    # 5. POST-TOOL LINTER: CONTRACT & ADVERSARIAL INPUTS
    # ==========================================
    def test_post_tool_linter_normal_payload(self):
        """Assert post_tool_linter returns empty dict on valid execution."""
        payload = {
            "stepIdx": 1,
            "toolCall": {"name": "run_command", "args": {"CommandLine": "pytest"}},
            "error": "",
            "conversationId": "conv-123",
        }
        res = self._execute_hook_json(self.post_tool_script, payload)
        self.assertEqual(res, {})

    def test_post_tool_linter_with_error(self):
        """Assert post_tool_linter captures error, logs to stderr, and returns empty dict."""
        payload = {
            "stepIdx": 2,
            "toolCall": {"name": "run_command", "args": {"CommandLine": "pytest"}},
            "error": "SyntaxError in line 42",
            "conversationId": "conv-123",
        }
        code, stdout, stderr = self._execute_hook_raw(self.post_tool_script, json.dumps(payload))
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(stdout.strip()), {})
        self.assertIn("SyntaxError in line 42", stderr)

    def test_post_tool_linter_malformed_inputs_never_crash(self):
        """Assert post_tool_linter never crashes on malformed inputs."""
        malformed = [
            "",
            "   ",
            "{bad: json",
            "null",
            "999",
            '["array"]',
            '{"stepIdx": "not_an_int", "error": null}',
            '{"stepIdx": null, "error": 12345}',
        ]
        for inp in malformed:
            with self.subTest(sample=inp[:20]):
                code, stdout, stderr = self._execute_hook_raw(self.post_tool_script, inp)
                self.assertEqual(code, 0, f"PostToolLinter crashed on input: {inp}. Stderr: {stderr}")
                try:
                    res = json.loads(stdout.strip())
                    self.assertIsInstance(res, dict)
                except Exception as e:
                    self.fail(f"PostToolLinter did not return valid JSON. Error: {e}")

    # ==========================================
    # 6. STOP GATEKEEPER: INVARIANTS & ADVERSARIAL INPUTS
    # ==========================================
    def test_stop_gatekeeper_active_background_tasks(self):
        """Assert stop_gatekeeper returns continue when background tasks are running."""
        payload = {
            "terminationReason": "model_stop",
            "fullyIdle": False,
            "conversationId": "conv-001"
        }
        res = self._execute_hook_json(self.stop_script, payload)
        self.assertEqual(res.get("decision"), "continue")

    def test_stop_gatekeeper_idle_tasks(self):
        """Assert stop_gatekeeper permits stop when fully idle."""
        payload = {
            "terminationReason": "model_stop",
            "fullyIdle": True,
            "conversationId": "conv-001"
        }
        res = self._execute_hook_json(self.stop_script, payload)
        self.assertEqual(res.get("decision"), "stop")

    def test_stop_gatekeeper_other_reasons(self):
        """Assert stop_gatekeeper permits stop on user_cancel or error regardless of idle state."""
        for reason in ["user_cancel", "error", "max_turns"]:
            with self.subTest(reason=reason):
                payload = {
                    "terminationReason": reason,
                    "fullyIdle": False,
                    "conversationId": "conv-001"
                }
                res = self._execute_hook_json(self.stop_script, payload)
                self.assertEqual(res.get("decision"), "stop")

    def test_stop_gatekeeper_malformed_inputs_never_crash(self):
        """Assert stop_gatekeeper never crashes on malformed inputs."""
        malformed = [
            "",
            "   ",
            "{broken",
            "null",
            "123",
            '["list"]',
            '{"terminationReason": null, "fullyIdle": null}',
            '{"terminationReason": 123, "fullyIdle": "not_a_bool"}',
        ]
        for inp in malformed:
            with self.subTest(sample=inp[:20]):
                code, stdout, stderr = self._execute_hook_raw(self.stop_script, inp)
                self.assertEqual(code, 0, f"StopGatekeeper crashed on input: {inp}. Stderr: {stderr}")
                try:
                    res = json.loads(stdout.strip())
                    self.assertIsInstance(res, dict)
                    self.assertIn("decision", res)
                except Exception as e:
                    self.fail(f"StopGatekeeper did not return valid JSON. Error: {e}")

    # ==========================================
    # 7. MANIFESTS & CONFIG SCHEMAS
    # ==========================================
    def test_plugin_json_schema(self):
        """Assert plugin.json contains valid Antigravity 2.0 schema."""
        plugin_file = PLUGIN_ROOT / "plugin.json"
        self.assertTrue(plugin_file.exists())
        with open(plugin_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertEqual(data.get("name"), "agi-antigravity-core")
        self.assertRegex(data.get("version", ""), r"^\d+\.\d+\.\d+$")
        self.assertIsInstance(data.get("description"), str)
        self.assertGreater(len(data.get("description")), 10)
        self.assertIn("author", data)
        self.assertIn("name", data["author"])
        self.assertIn("license", data)
        self.assertIsInstance(data.get("keywords"), list)
        self.assertGreaterEqual(len(data["keywords"]), 5)

    def test_mcp_config_json_schema(self):
        """Assert mcp_config.json contains valid MCP server configurations."""
        mcp_file = PLUGIN_ROOT / "mcp_config.json"
        self.assertTrue(mcp_file.exists())
        with open(mcp_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("mcpServers", data)
        servers = data["mcpServers"]
        self.assertIn("puppeteer", servers)
        self.assertIn("chrome-devtools", servers)
        for sname, sdef in servers.items():
            self.assertIn("command", sdef)
            self.assertIn("args", sdef)
            self.assertIsInstance(sdef["args"], list)

    def test_hooks_json_schema_and_commands(self):
        """Assert hooks.json maps valid events and target files exist."""
        hooks_file = PLUGIN_ROOT / "hooks.json"
        self.assertTrue(hooks_file.exists())
        with open(hooks_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIn("pre-tool-validator", data)
        self.assertIn("post-tool-linter", data)
        self.assertIn("stop-gatekeeper", data)


if __name__ == "__main__":
    unittest.main()
