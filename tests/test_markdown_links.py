"""
Suite 3: Markdown Hyperlink and Cross-Reference Integrity Validation.
Scans all markdown files in the package and asserts 100% resolution of all relative links and file targets (0 broken links).
"""
import re
import unittest
from pathlib import Path
from typing import List, NamedTuple, Optional, Tuple

try:
    from conftest import PLUGIN_ROOT
except ImportError:
    from .conftest import PLUGIN_ROOT


class LinkOccurrence(NamedTuple):
    source_file: Path
    line_number: int
    raw_target: str
    resolved_path: Path
    error_reason: str


class TestMarkdownLinks(unittest.TestCase):
    """Tier 3: Markdown relative link and reference integrity tests."""

    # Regex matching markdown links: [text](target) and ![alt](target)
    LINK_REGEX = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")

    @classmethod
    def setUpClass(cls):
        cls.md_files = list(PLUGIN_ROOT.rglob("*.md"))
        # Exclude temporary or test artifacts if any
        cls.md_files = [
            f for f in cls.md_files if not any(p.startswith(".") for p in f.parts)
        ]

    def test_markdown_files_exist(self):
        """Validates that markdown documentation files exist across the plugin."""
        self.assertTrue(
            len(self.md_files) > 0,
            f"No markdown files found under {PLUGIN_ROOT}",
        )

    def test_zero_broken_relative_links(self):
        """Extracts all relative markdown link targets and asserts 100% resolve to valid files on disk."""
        broken_links: List[LinkOccurrence] = []
        total_links_checked = 0

        for md_file in self.md_files:
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception as e:
                broken_links.append(
                    LinkOccurrence(
                        source_file=md_file,
                        line_number=1,
                        raw_target="",
                        resolved_path=md_file,
                        error_reason=f"Failed to read file: {e}",
                    )
                )
                continue

            lines = content.splitlines()
            for line_idx, line in enumerate(lines, start=1):
                # Find all links in line
                for match in self.LINK_REGEX.finditer(line):
                    raw_target = match.group(2).strip()

                    # Strip optional title in quotes: [text](target "title")
                    if " " in raw_target:
                        raw_target = raw_target.split()[0].strip()

                    # Strip angle brackets: [<target>]
                    if raw_target.startswith("<") and raw_target.endswith(">"):
                        raw_target = raw_target[1:-1].strip()

                    # Skip empty targets
                    if not raw_target:
                        continue

                    # Skip external URLs and protocols
                    if any(
                        raw_target.lower().startswith(proto)
                        for proto in ("http://", "https://", "mailto:", "ftp:", "data:", "tel:")
                    ):
                        continue

                    # Handle pure in-file anchor links (e.g. #my-heading)
                    if raw_target.startswith("#"):
                        # In-file anchor check
                        anchor_slug = raw_target[1:].lower().strip()
                        if anchor_slug:
                            if not self._heading_exists(content, anchor_slug):
                                broken_links.append(
                                    LinkOccurrence(
                                        source_file=md_file,
                                        line_number=line_idx,
                                        raw_target=raw_target,
                                        resolved_path=md_file,
                                        error_reason=f"In-page anchor '{raw_target}' not found in {md_file.name}",
                                    )
                                )
                        total_links_checked += 1
                        continue

                    # Split path and anchor (e.g. ./path/file.md#heading)
                    target_path_part = raw_target
                    anchor_part: Optional[str] = None
                    if "#" in raw_target:
                        target_path_part, anchor_part = raw_target.split("#", 1)

                    if not target_path_part:
                        continue

                    total_links_checked += 1

                    # Resolve relative target against source file directory
                    try:
                        # Handle posix separators on Windows
                        clean_rel_path = target_path_part.replace("/", "\\")
                        resolved = (md_file.parent / clean_rel_path).resolve()
                    except Exception as e:
                        broken_links.append(
                            LinkOccurrence(
                                source_file=md_file,
                                line_number=line_idx,
                                raw_target=raw_target,
                                resolved_path=md_file.parent / target_path_part,
                                error_reason=f"Path resolution error: {e}",
                            )
                        )
                        continue

                    if not resolved.exists():
                        broken_links.append(
                            LinkOccurrence(
                                source_file=md_file,
                                line_number=line_idx,
                                raw_target=raw_target,
                                resolved_path=resolved,
                                error_reason="Target file does not exist on disk",
                            )
                        )
                    elif anchor_part and resolved.suffix.lower() == ".md":
                        # Validate anchor in target markdown file
                        try:
                            target_content = resolved.read_text(encoding="utf-8")
                            if not self._heading_exists(target_content, anchor_part.lower()):
                                broken_links.append(
                                    LinkOccurrence(
                                        source_file=md_file,
                                        line_number=line_idx,
                                        raw_target=raw_target,
                                        resolved_path=resolved,
                                        error_reason=f"Anchor '#{anchor_part}' not found in target file {resolved.name}",
                                    )
                                )
                        except Exception as e:
                            broken_links.append(
                                LinkOccurrence(
                                    source_file=md_file,
                                    line_number=line_idx,
                                    raw_target=raw_target,
                                    resolved_path=resolved,
                                    error_reason=f"Cannot inspect target file anchor: {e}",
                                )
                            )

        # Build diagnostic report if broken links exist
        if broken_links:
            report_lines = [
                f"\nFound {len(broken_links)} broken markdown link(s) across {len(self.md_files)} files (total links checked: {total_links_checked}):"
            ]
            for link in broken_links:
                try:
                    rel_src = link.source_file.relative_to(PLUGIN_ROOT)
                except ValueError:
                    rel_src = link.source_file
                report_lines.append(
                    f"  - {rel_src}:{link.line_number} -> target: '{link.raw_target}' (Resolved: '{link.resolved_path}') Reason: {link.error_reason}"
                )
            self.fail("\n".join(report_lines))

    def _heading_exists(self, content: str, anchor_slug: str) -> bool:
        """Checks if a markdown heading corresponding to anchor_slug exists in content."""
        # Clean slug (remove punctuation, replace spaces with hyphens)
        clean_anchor = re.sub(r"[^\w\- ]", "", anchor_slug).strip().replace(" ", "-").lower()

        for line in content.splitlines():
            line_str = line.strip()
            if line_str.startswith("#"):
                heading_text = line_str.lstrip("#").strip()
                heading_slug = re.sub(r"[^\w\- ]", "", heading_text).strip().replace(" ", "-").lower()
                if heading_slug == clean_anchor or clean_anchor in heading_slug:
                    return True
                # Direct match
                if clean_anchor in heading_text.lower():
                    return True
        return False


if __name__ == "__main__":
    unittest.main()
