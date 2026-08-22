"""
Suite 4: Zero-Placeholder & Production-Hygiene Policy Validation.
Scans the entire codebase for forbidden stubs, TODOs, mock data, and placeholder constructs.
Asserts zero violations across all production skills, rules, hooks, manifests, and scripts.
"""
import os
import re
import unittest
from pathlib import Path
from typing import List, NamedTuple

try:
    from conftest import FORBIDDEN_PLACEHOLDER_PATTERNS, PLUGIN_ROOT
except ImportError:
    from .conftest import FORBIDDEN_PLACEHOLDER_PATTERNS, PLUGIN_ROOT


class PlaceholderViolation(NamedTuple):
    file_path: Path
    line_number: int
    matched_pattern: str
    description: str
    line_snippet: str


class TestZeroPlaceholders(unittest.TestCase):
    """Tier 3: Codebase hygiene and zero-placeholder enforcement tests."""

    EXCLUDED_DIRS = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        "tests",  # Test suite itself contains test pattern definitions
        "node_modules",
        ".venv",
        "venv",
    }

    ALLOWED_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".json",
        ".md",
        ".sh",
        ".bash",
        ".ps1",
        ".yaml",
        ".yml",
        ".toml",
    }

    def _collect_production_files(self) -> List[Path]:
        """Collects all production files in the plugin, ignoring tests and caches."""
        production_files: List[Path] = []
        for root, dirs, files in os.walk(PLUGIN_ROOT):
            # Modify dirs in-place to prevent descending into excluded dirs
            dirs[:] = [d for d in dirs if d not in self.EXCLUDED_DIRS and not d.startswith(".")]

            for file in files:
                file_path = Path(root) / file
                if file_path.suffix.lower() in self.ALLOWED_EXTENSIONS:
                    production_files.append(file_path)

        return production_files

    def test_zero_placeholders_in_codebase(self):
        """Scans all production files and asserts 0 placeholder or stub violations."""
        files_to_scan = self._collect_production_files()
        self.assertTrue(
            len(files_to_scan) > 0,
            f"No production files found to scan in {PLUGIN_ROOT}",
        )

        violations: List[PlaceholderViolation] = []

        compiled_patterns = [
            (re.compile(pattern, re.IGNORECASE), pattern, desc)
            for pattern, desc in FORBIDDEN_PLACEHOLDER_PATTERNS
        ]

        for file_path in files_to_scan:
            try:
                content = file_path.read_text(encoding="utf-8")
            except Exception as e:
                # If file cannot be read as utf-8, skip binary-like files
                continue

            lines = content.splitlines()
            for line_idx, line in enumerate(lines, start=1):
                # Skip markdown documentation lines that are explicitly discussing the placeholder rule / policy
                if file_path.suffix.lower() == ".md":
                    line_lower = line.lower()
                    if (
                        "forbidden" in line_lower
                        or "banned" in line_lower
                        or "zero placeholder" in line_lower
                        or "zero-placeholder" in line_lower
                        or "prohibition" in line_lower
                        or "policy" in line_lower
                        or "mandate" in line_lower
                    ):
                        continue

                for regex, pattern_str, desc in compiled_patterns:
                    match = regex.search(line)
                    if match:
                        # Extra guard for documentation referencing backticked tokens in markdown
                        if file_path.suffix.lower() == ".md" and f"`{match.group(0)}`" in line:
                            continue

                        violations.append(
                            PlaceholderViolation(
                                file_path=file_path,
                                line_number=line_idx,
                                matched_pattern=pattern_str,
                                description=desc,
                                line_snippet=line.strip(),
                            )
                        )

        if violations:
            report_lines = [
                f"\nFound {len(violations)} forbidden placeholder/stub violation(s) across {len(files_to_scan)} production files:"
            ]
            for v in violations:
                try:
                    rel_path = v.file_path.relative_to(PLUGIN_ROOT)
                except ValueError:
                    rel_path = v.file_path
                report_lines.append(
                    f"  - {rel_path}:{v.line_number} [{v.description}] -> \"{v.line_snippet}\""
                )
            self.fail("\n".join(report_lines))


if __name__ == "__main__":
    unittest.main()
