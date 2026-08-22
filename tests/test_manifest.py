"""
Suite 1: Manifest, MCP Configuration, Hooks, and Rules Schema Validation.
Validates plugin.json, mcp_config.json, hooks.json, and rules/AGENTS.md against Antigravity specifications.
"""
import json
import re
import unittest
from pathlib import Path

try:
    from conftest import PLUGIN_ROOT
except ImportError:
    from .conftest import PLUGIN_ROOT


class TestManifestsAndSchemas(unittest.TestCase):
    """Tier 1: Manifest, MCP config, hooks, and rules schema tests."""

    def test_plugin_json_exists_and_valid(self):
        """Validates plugin.json presence, JSON validity, semver, and required metadata."""
        plugin_file = PLUGIN_ROOT / "plugin.json"
        self.assertTrue(
            plugin_file.exists(), f"plugin.json not found at {plugin_file}"
        )

        with open(plugin_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIsInstance(data, dict, "plugin.json must be a JSON object")

        # Name validation
        self.assertIn("name", data, "plugin.json must contain 'name'")
        self.assertIsInstance(data["name"], str, "'name' must be a string")
        self.assertEqual(
            data["name"],
            "agi-antigravity-core",
            f"Expected plugin name 'agi-antigravity-core', got '{data.get('name')}'",
        )

        # Version validation (SemVer X.Y.Z)
        self.assertIn("version", data, "plugin.json must contain 'version'")
        version = data["version"]
        self.assertIsInstance(version, str, "'version' must be a string")
        semver_pattern = r"^\d+\.\d+\.\d+(-[a-zA-Z0-9.-]+)?$"
        self.assertTrue(
            re.match(semver_pattern, version),
            f"Version '{version}' is not valid SemVer (e.g. 1.0.0)",
        )

        # Description validation
        self.assertIn("description", data, "plugin.json must contain 'description'")
        self.assertIsInstance(
            data["description"], str, "'description' must be a string"
        )
        self.assertTrue(
            len(data["description"].strip()) > 10,
            "Description must be informative and non-trivial (>10 characters)",
        )

        # Keywords validation
        if "keywords" in data:
            self.assertIsInstance(
                data["keywords"], list, "'keywords' must be a list of strings"
            )
            for kw in data["keywords"]:
                self.assertIsInstance(kw, str, f"Keyword '{kw}' must be a string")

        # Author validation
        if "author" in data:
            self.assertTrue(
                isinstance(data["author"], (dict, str)),
                "'author' must be a string or object",
            )

    def test_mcp_config_json_schema(self):
        """Validates mcp_config.json structure, transport types (stdio / sse), and server definitions."""
        mcp_file = PLUGIN_ROOT / "mcp_config.json"
        self.assertTrue(
            mcp_file.exists(), f"mcp_config.json not found at {mcp_file}"
        )

        with open(mcp_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIsInstance(data, dict, "mcp_config.json must be a JSON object")
        self.assertIn(
            "mcpServers",
            data,
            "mcp_config.json must contain top-level 'mcpServers' object",
        )
        self.assertIsInstance(
            data["mcpServers"], dict, "'mcpServers' must be a dictionary"
        )
        self.assertTrue(
            len(data["mcpServers"]) > 0,
            "At least one MCP server should be defined in mcpServers",
        )

        for server_name, server_cfg in data["mcpServers"].items():
            self.assertIsInstance(
                server_cfg,
                dict,
                f"Server config for '{server_name}' must be a dictionary",
            )

            # Server must be stdio (has 'command') or sse (has 'serverUrl')
            has_command = "command" in server_cfg
            has_url = "serverUrl" in server_cfg

            self.assertTrue(
                has_command or has_url,
                f"MCP server '{server_name}' must declare either 'command' (stdio) or 'serverUrl' (sse)",
            )

            if has_command:
                self.assertIsInstance(
                    server_cfg["command"],
                    str,
                    f"'command' for '{server_name}' must be a string",
                )
                if "args" in server_cfg:
                    self.assertIsInstance(
                        server_cfg["args"],
                        list,
                        f"'args' for '{server_name}' must be a list of strings",
                    )
                    for arg in server_cfg["args"]:
                        self.assertIsInstance(
                            arg, str, f"Arg '{arg}' in '{server_name}' must be string"
                        )
                if "env" in server_cfg:
                    self.assertIsInstance(
                        server_cfg["env"],
                        dict,
                        f"'env' for '{server_name}' must be an object",
                    )

            if has_url:
                self.assertIsInstance(
                    server_cfg["serverUrl"],
                    str,
                    f"'serverUrl' for '{server_name}' must be a string",
                )
                self.assertTrue(
                    server_cfg["serverUrl"].startswith("http://")
                    or server_cfg["serverUrl"].startswith("https://"),
                    f"'serverUrl' for '{server_name}' must start with http:// or https://",
                )

    def test_hooks_json_schema(self):
        """Validates hooks.json schema, lifecycle events, matchers, and command structure."""
        hooks_file = PLUGIN_ROOT / "hooks.json"
        self.assertTrue(hooks_file.exists(), f"hooks.json not found at {hooks_file}")

        with open(hooks_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.assertIsInstance(data, dict, "hooks.json must be a JSON object")

        valid_events = {
            "PreToolUse",
            "PostToolUse",
            "PreInvocation",
            "PostInvocation",
            "Stop",
        }

        for hook_name, hook_spec in data.items():
            self.assertIsInstance(
                hook_spec, dict, f"Hook '{hook_name}' must be a dictionary"
            )

            if "enabled" in hook_spec:
                self.assertIsInstance(
                    hook_spec["enabled"],
                    bool,
                    f"'enabled' in hook '{hook_name}' must be boolean",
                )

            # Check event lists
            for event_name, event_handlers in hook_spec.items():
                if event_name == "enabled":
                    continue

                self.assertIn(
                    event_name,
                    valid_events,
                    f"Unknown event '{event_name}' in hook '{hook_name}'. Valid: {valid_events}",
                )
                self.assertIsInstance(
                    event_handlers,
                    list,
                    f"Event '{event_name}' in hook '{hook_name}' must be a list",
                )

                if event_name in ("PreToolUse", "PostToolUse"):
                    # Grouped structure with matcher
                    for group in event_handlers:
                        self.assertIsInstance(
                            group,
                            dict,
                            f"Grouped handler in {event_name} of {hook_name} must be a dict",
                        )
                        self.assertIn(
                            "matcher",
                            group,
                            f"Missing 'matcher' in {event_name} of {hook_name}",
                        )
                        self.assertIn(
                            "hooks",
                            group,
                            f"Missing 'hooks' list in {event_name} of {hook_name}",
                        )
                        self.assertIsInstance(
                            group["hooks"],
                            list,
                            f"'hooks' in {event_name} of {hook_name} must be a list",
                        )
                        for h in group["hooks"]:
                            self._validate_hook_handler(h, hook_name, event_name)
                else:
                    # Flat handler objects
                    for h in event_handlers:
                        self._validate_hook_handler(h, hook_name, event_name)

    def _validate_hook_handler(
        self, handler: dict, hook_name: str, event_name: str
    ):
        """Helper to validate an individual hook handler object."""
        self.assertIsInstance(
            handler,
            dict,
            f"Handler in {event_name} of {hook_name} must be a dictionary",
        )
        self.assertIn(
            "command",
            handler,
            f"Hook handler in {event_name} of {hook_name} must specify 'command'",
        )
        self.assertIsInstance(
            handler["command"],
            str,
            f"'command' in {event_name} of {hook_name} must be a string",
        )

        if "type" in handler:
            self.assertEqual(
                handler["type"],
                "command",
                f"Unsupported hook type '{handler['type']}' in {hook_name}. Only 'command' supported.",
            )

        if "timeout" in handler:
            self.assertIsInstance(
                handler["timeout"],
                int,
                f"'timeout' in {hook_name} must be an integer",
            )
            self.assertTrue(
                handler["timeout"] > 0,
                f"'timeout' in {hook_name} must be positive (> 0)",
            )

    def test_rules_agents_md_exists_and_conforms(self):
        """Validates rules/AGENTS.md existence, size, and presence of mandatory constitutional dogmas."""
        rules_file = PLUGIN_ROOT / "rules" / "AGENTS.md"
        self.assertTrue(
            rules_file.exists(), f"rules/AGENTS.md not found at {rules_file}"
        )

        content = rules_file.read_text(encoding="utf-8")
        lines = content.splitlines()

        self.assertTrue(
            len(lines) >= 20,
            f"rules/AGENTS.md is too short ({len(lines)} lines). Expected comprehensive rules.",
        )

        # Constitutional checks
        content_upper = content.upper()
        # 1. 5 Cognitive Modes or Mode distinction
        self.assertTrue(
            "MODE:" in content or "[MODE" in content or "COGNITIVE MODES" in content_upper,
            "rules/AGENTS.md must define cognitive operating modes (e.g. BUILD, DEBUG, RESEARCH, GAUNTLET)",
        )
        # 2. Concurrency limit or governance
        self.assertTrue(
            "C_MAX" in content_upper or "CONCURRENCY" in content_upper or "SUBAGENT" in content_upper,
            "rules/AGENTS.md must define subagent concurrency and delegation rules",
        )
        # 3. Zero-Guessing / TDD / Verification
        self.assertTrue(
            "ZERO-GUESS" in content_upper or "TDD" in content_upper or "VERIF" in content_upper,
            "rules/AGENTS.md must mandate zero-guessing and rigorous verification",
        )

    def test_readme_and_project_brain_exist(self):
        """Validates README.md and PROJECT_BRAIN.md existence and basic documentation integrity."""
        readme = PLUGIN_ROOT / "README.md"
        self.assertTrue(readme.exists(), f"README.md not found at {readme}")
        self.assertTrue(len(readme.read_text(encoding="utf-8").strip()) > 100)

        brain = PLUGIN_ROOT / "PROJECT_BRAIN.md"
        self.assertTrue(brain.exists(), f"PROJECT_BRAIN.md not found at {brain}")
        self.assertTrue(len(brain.read_text(encoding="utf-8").strip()) > 100)


if __name__ == "__main__":
    unittest.main()
