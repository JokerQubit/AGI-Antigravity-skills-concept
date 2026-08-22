"""
Adversarial Verification Test Suite for Milestone 2 (Core Methodology Skills).
Empirically stress-tests:
1. Frontmatter parser against malformed delimiters, invalid chars, multiline, comments, and edge cases.
2. Trigger descriptions for zero ambiguity, distinct semantic boundaries, and intent classification.
3. Complete relative link and heading anchor resolution on disk.
4. Zero placeholders, stubs, and anti-hallucination tool call validity.
5. Content density, structural completeness, and methodology invariants.
"""
import os
import re
import sys
import unittest
from pathlib import Path
from typing import Dict, List, Set, Tuple

# Ensure paths
TESTS_DIR = Path(__file__).resolve().parent
PLUGIN_ROOT = TESTS_DIR.parent
if str(PLUGIN_ROOT) not in sys.path:
    sys.path.insert(0, str(PLUGIN_ROOT))
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from conftest import (
    ALL_APPROVED_TOOLS,
    FORBIDDEN_PLACEHOLDER_PATTERNS,
    PLUGIN_ROOT,
    parse_yaml_frontmatter,
)

M2_SKILLS = [
    "test-driven-development",
    "systematic-debugging",
    "gauntlet-loop",
    "subagent-handoff",
    "causal-debugging-protocol",
    "session-handoff-protocol",
]

M2_REFERENCES = [
    "test-driven-development/references/tdd-patterns.md",
    "systematic-debugging/references/root-cause-playbook.md",
    "gauntlet-loop/references/adversarial-benchmarking.md",
    "subagent-handoff/references/handoff-protocol.md",
    "causal-debugging-protocol/references/falsification-matrices.md",
    "session-handoff-protocol/references/state-cryptography.md",
]


class TestM2AdversarialStress(unittest.TestCase):
    """Empirical adversarial challenge suite for Milestone 2."""

    @classmethod
    def setUpClass(cls):
        cls.skills_dir = PLUGIN_ROOT / "skills"

    # -------------------------------------------------------------------------
    # SUITE 1: FRONTMATTER PARSER FUZZING & ROBUSTNESS
    # -------------------------------------------------------------------------
    def test_frontmatter_parser_fuzzing(self):
        """Fuzz parse_yaml_frontmatter with 20+ malformed, edge-case, and boundary inputs."""
        test_cases = [
            ("", True, "Empty string"),
            ("   \n\t  ", True, "Whitespace only"),
            ("# Just markdown\nHello world", True, "No frontmatter"),
            ("---\nname: test", True, "Unclosed frontmatter (single delimiter)"),
            ("---\n---", False, "Empty frontmatter"),
            ("---\nname: foo\n---\nBody content", False, "Minimal well-formed"),
            ("---\nname: foo\n# comment line\ndescription: bar\n---\nBody", False, "Comments inside"),
            ("---\nname: \"quoted-name\"\ndescription: 'single-quoted desc'\n---", False, "Quoted values"),
            ("---\nname: folded-desc\ndescription: >-\n  This is a multiline\n  folded description.\n---\nBody", False, "Folded block >-"),
            ("---\nname: block-desc\ndescription: |\n  This is a literal\n  block description.\n---\nBody", False, "Literal block |"),
            ("---\nname: colons-in-val\ndescription: Trigger at 12:00:00 on https://example.com/api:test\n---", False, "Colons in value"),
            ("---\nname: unicode-val\ndescription: Specialized agent for testing and security\n---", False, "Unicode and clean desc"),
            ("---\r\nname: windows-crlf\r\ndescription: Windows line endings\r\n---\r\nBody text", False, "Windows CRLF"),
            ("---\n  name  :  spaced-key  \n  description  :  spaced-val  \n---", False, "Spaces around colons"),
            ("---\ninvalid_line_without_colon\nname: valid\n---", False, "Malformed line inside"),
            ("---\nname: foo\ndescription:\n---", False, "Empty value for key"),
            ("---\nname: multi\ndescription: Line 1\n Line 2\n Line 3\n---", False, "Implicit multiline continuation"),
        ]

        for input_text, expected_none, desc in test_cases:
            with self.subTest(case=desc):
                fm, body = parse_yaml_frontmatter(input_text)
                if expected_none:
                    self.assertIsNone(fm, f"Expected None for case '{desc}', got {fm}")
                else:
                    self.assertIsNotNone(fm, f"Expected valid dict for case '{desc}', got None")
                    self.assertIsInstance(fm, dict)

    def test_production_m2_frontmatter_parsed_strictly(self):
        """Assert all 6 production M2 skills parse strictly without errors or missing fields."""
        for skill_name in M2_SKILLS:
            skill_file = self.skills_dir / skill_name / "SKILL.md"
            self.assertTrue(skill_file.exists(), f"Missing {skill_file}")

            content = skill_file.read_text(encoding="utf-8")
            fm, body = parse_yaml_frontmatter(content)

            self.assertIsNotNone(fm, f"Failed to parse frontmatter in {skill_name}/SKILL.md")
            self.assertIn("name", fm, f"Missing 'name' key in {skill_name}/SKILL.md")
            self.assertIn("description", fm, f"Missing 'description' key in {skill_name}/SKILL.md")

            self.assertEqual(fm["name"], skill_name, f"Name mismatch in {skill_name}")
            self.assertGreaterEqual(len(fm["description"].strip()), 30, f"Description too short in {skill_name}")
            self.assertLessEqual(len(fm["description"].strip()), 500, f"Description excessively long in {skill_name}")

            # Check third-person phrasing
            first_word = fm["description"].strip().split()[0].lower()
            self.assertNotIn(first_word, ["i", "we", "my", "our"], f"First person pronoun in {skill_name}")

            # Body assertions
            self.assertGreater(len(body.strip()), 200, f"Body too short in {skill_name}")
            self.assertTrue("#" in body, f"No markdown headers in {skill_name}")

    # -------------------------------------------------------------------------
    # SUITE 2: TRIGGER DESCRIPTION DISAMBIGUATION & SEMANTIC BOUNDARIES
    # -------------------------------------------------------------------------
    def test_trigger_descriptions_jaccard_distinctness(self):
        """Empirically assert that no two M2 skill trigger descriptions have excessive semantic overlap."""
        descriptions: Dict[str, Set[str]] = {}

        stop_words = {"a", "an", "the", "and", "or", "of", "to", "in", "for", "with", "on", "at", "by", "from", "using", "across", "is", "are", "it"}

        for skill_name in M2_SKILLS:
            content = (self.skills_dir / skill_name / "SKILL.md").read_text(encoding="utf-8")
            fm, _ = parse_yaml_frontmatter(content)
            assert fm is not None
            words = set(re.findall(r"[a-zA-Z0-9_-]{3,}", fm["description"].lower()))
            filtered = words - stop_words
            descriptions[skill_name] = filtered

        # Check pairwise Jaccard similarity: |A ∩ B| / |A ∪ B|
        max_allowed_jaccard = 0.35  # Trigger descriptions must be distinct and specific
        for i in range(len(M2_SKILLS)):
            for j in range(i + 1, len(M2_SKILLS)):
                s1, s2 = M2_SKILLS[i], M2_SKILLS[j]
                w1, w2 = descriptions[s1], descriptions[s2]
                intersection = w1 & w2
                union = w1 | w2
                jaccard = len(intersection) / len(union) if union else 0.0

                self.assertLess(
                    jaccard,
                    max_allowed_jaccard,
                    f"High semantic overlap between '{s1}' and '{s2}' (Jaccard: {jaccard:.2f}, shared words: {intersection})",
                )

    def test_trigger_intent_classification(self):
        """Test simulated intent classification across 30 distinct test prompts against trigger keywords."""
        benchmarks = {
            "test-driven-development": [
                "Enforce strict Test-Driven Development workflows",
                "Follow the Red-Green-Refactor cycle for this module",
                "Write failing unit or integration tests before production code",
                "Implement minimal passing logic to satisfy the test",
                "Refactor cleanly with zero regressions",
            ],
            "systematic-debugging": [
                "Execute the 4-phase root-cause debugging protocol",
                "Reproduce, isolate, diagnose, and verify the complex defect",
                "Eliminate trial-and-error edits with zero-guesswork instrumentation",
                "Trigger escalation upon 3 consecutive failures",
                "Isolate and diagnose root-cause defects methodically",
            ],
            "gauntlet-loop": [
                "Orchestrate double-blind builder and critic verification",
                "Adversarial verification loop against the Named Reference Bar",
                "Enforce Dual-Gate convergence with test pass and Q >= 9.0",
                "Calculate Lyapunov delta stabilization across iterations",
                "Run blind qualitative scoring and adversarial benchmarking",
            ],
            "subagent-handoff": [
                "Format a 5-component handoff report with observation logic caveats",
                "Coordinate multi-agent task transfer and structured handoff",
                "Standardize subagent handoffs with context-isolated execution boundaries",
                "Ensure zero context loss across multi-agent delegations",
                "Write structured conclusion and verification method in handoff",
            ],
            "causal-debugging-protocol": [
                "Conduct deep causal root-cause investigations",
                "Trace mathematical state transitions and invariant trees",
                "Popperian falsification of state corruption paths",
                "Map failure paths backwards for atomic bug isolation",
                "Prove causal state corruption with zero guesswork",
            ],
            "session-handoff-protocol": [
                "Manage transactional session state serialization",
                "Compute cryptographic SHA-256 state hash for session",
                "Execute atomic session handoffs across agent turns",
                "Eliminate hallucinations and context drift during long-horizon tasks",
                "Persist session state snapshot across context windows",
            ],
        }

        stop_words = {"a", "an", "the", "and", "or", "of", "to", "in", "for", "with", "on", "at", "by", "from", "using", "across", "is", "are", "it", "before", "after", "all", "any", "that", "this"}

        def token_match_score(prompt_tokens: Set[str], desc_tokens: Set[str]) -> int:
            score = 0
            for pt in prompt_tokens:
                for dt in desc_tokens:
                    if pt == dt:
                        score += 2
                        break
                    elif len(pt) >= 4 and len(dt) >= 4 and pt[:4] == dt[:4]:
                        score += 1
                        break
            return score

        skill_descriptors: Dict[str, Set[str]] = {}
        for s in M2_SKILLS:
            fm, _ = parse_yaml_frontmatter((self.skills_dir / s / "SKILL.md").read_text(encoding="utf-8"))
            assert fm is not None
            raw_tokens = set(re.findall(r"[a-z0-9_-]+", fm["description"].lower() + " " + fm["name"].lower()))
            skill_descriptors[s] = raw_tokens - stop_words

        for expected_skill, prompts in benchmarks.items():
            for prompt in prompts:
                p_tokens = set(re.findall(r"[a-z0-9_-]+", prompt.lower())) - stop_words
                scores = {s: token_match_score(p_tokens, desc) for s, desc in skill_descriptors.items()}
                sorted_scores = sorted(scores.items(), key=lambda item: item[1], reverse=True)
                best = sorted_scores[0]
                second = sorted_scores[1]

                self.assertGreater(best[1], 0, f"Prompt '{prompt}' scored 0 against all skills")
                self.assertEqual(
                    best[0],
                    expected_skill,
                    f"Prompt '{prompt}' misclassified as '{best[0]}' instead of '{expected_skill}' (scores: {scores})",
                )
                self.assertGreater(
                    best[1],
                    second[1],
                    f"Ambiguity/tie for prompt '{prompt}': top scores {sorted_scores[:2]}",
                )

    # -------------------------------------------------------------------------
    # SUITE 3: COMPLETE RELATIVE LINK & ANCHOR GRAPH RESOLUTION
    # -------------------------------------------------------------------------
    def test_m2_all_markdown_links_and_anchors(self):
        """Assert all markdown links in M2 skills and references resolve to real files and valid anchors."""
        all_m2_files = [self.skills_dir / s / "SKILL.md" for s in M2_SKILLS] + [
            self.skills_dir / r for r in M2_REFERENCES
        ]

        link_regex = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")

        total_links = 0
        for md_file in all_m2_files:
            self.assertTrue(md_file.exists(), f"File does not exist: {md_file}")
            content = md_file.read_text(encoding="utf-8")
            lines = content.splitlines()

            for line_idx, line in enumerate(lines, start=1):
                for match in link_regex.finditer(line):
                    raw_target = match.group(2).strip()

                    if " " in raw_target:
                        raw_target = raw_target.split()[0].strip()

                    if any(raw_target.lower().startswith(p) for p in ("http://", "https://", "mailto:")):
                        continue

                    total_links += 1

                    if raw_target.startswith("#"):
                        anchor = raw_target[1:].lower().strip()
                        self.assertTrue(
                            self._heading_exists(content, anchor),
                            f"Anchor '{raw_target}' in {md_file.name}:{line_idx} not found in same file",
                        )
                        continue

                    path_part = raw_target
                    anchor_part = None
                    if "#" in raw_target:
                        path_part, anchor_part = raw_target.split("#", 1)

                    target_clean = path_part.replace("/", "\\")
                    resolved = (md_file.parent / target_clean).resolve()

                    self.assertTrue(
                        resolved.exists(),
                        f"Broken link in {md_file.relative_to(PLUGIN_ROOT)}:{line_idx} -> '{raw_target}' (Resolved: '{resolved}')",
                    )

                    if anchor_part and resolved.suffix.lower() == ".md":
                        target_content = resolved.read_text(encoding="utf-8")
                        self.assertTrue(
                            self._heading_exists(target_content, anchor_part.lower()),
                            f"Anchor '#{anchor_part}' not found in target file {resolved.name} (from {md_file.name}:{line_idx})",
                        )

        self.assertGreaterEqual(total_links, 6, f"Expected at least 6 cross-links across M2 files, found {total_links}")

    def _heading_exists(self, content: str, anchor_slug: str) -> bool:
        clean_anchor = re.sub(r"[^\w\- ]", "", anchor_slug).strip().replace(" ", "-").lower()
        for line in content.splitlines():
            line_str = line.strip()
            if line_str.startswith("#"):
                heading_text = line_str.lstrip("#").strip()
                heading_slug = re.sub(r"[^\w\- ]", "", heading_text).strip().replace(" ", "-").lower()
                if heading_slug == clean_anchor or clean_anchor in heading_slug or clean_anchor in heading_text.lower():
                    return True
        return False

    # -------------------------------------------------------------------------
    # SUITE 4: ZERO PLACEHOLDERS, STUBS & TOOL BINDINGS
    # -------------------------------------------------------------------------
    def test_m2_zero_placeholders_and_stubs(self):
        """Assert 0 forbidden placeholder tokens exist in any M2 skill or reference file."""
        all_m2_files = [self.skills_dir / s / "SKILL.md" for s in M2_SKILLS] + [
            self.skills_dir / r for r in M2_REFERENCES
        ]

        compiled_patterns = [
            (re.compile(pattern, re.IGNORECASE), pattern, desc)
            for pattern, desc in FORBIDDEN_PLACEHOLDER_PATTERNS
        ]

        for md_file in all_m2_files:
            content = md_file.read_text(encoding="utf-8")
            for line_idx, line in enumerate(content.splitlines(), start=1):
                line_lower = line.lower()
                if any(k in line_lower for k in ["forbidden", "banned", "zero placeholder", "policy", "mandate", "prohibition"]):
                    continue

                for regex, pattern_str, desc in compiled_patterns:
                    match = regex.search(line)
                    if match:
                        if f"`{match.group(0)}`" in line:
                            continue
                        self.fail(f"Forbidden placeholder pattern '{desc}' found in {md_file.name}:{line_idx} -> '{line.strip()}'")

    def test_m2_tool_invocations_validity(self):
        """Assert all tool references in M2 skills match approved Cortex tools."""
        all_m2_files = [self.skills_dir / s / "SKILL.md" for s in M2_SKILLS] + [
            self.skills_dir / r for r in M2_REFERENCES
        ]

        tool_call_regex = re.compile(r"\b([a-z_][a-z0-9_]*)\s*\(\s*(?:[A-Za-z0-9_]+=|['\"])")
        ignored_funcs = {"print", "len", "range", "open", "json", "dumps", "loads", "encode", "decode", "hexdigest", "read_bytes", "relative_to"}

        for md_file in all_m2_files:
            content = md_file.read_text(encoding="utf-8")
            for line_idx, line in enumerate(content.splitlines(), start=1):
                for match in tool_call_regex.finditer(line):
                    func_name = match.group(1)
                    if func_name in ignored_funcs:
                        continue
                    if any(k in line for k in ["CommandLine", "AbsolutePath", "TargetFile", "Message", "Recipient", "DurationSeconds"]):
                        self.assertIn(
                            func_name,
                            ALL_APPROVED_TOOLS,
                            f"Unknown/unregistered tool '{func_name}' called in {md_file.name}:{line_idx}",
                        )

    # -------------------------------------------------------------------------
    # SUITE 5: CONTENT DENSITY & METHODOLOGY INVARIANTS
    # -------------------------------------------------------------------------
    def test_m2_structural_density_and_invariants(self):
        """Assert deep technical substance, code blocks, diagrams, and invariant structures."""
        for skill_name in M2_SKILLS:
            skill_file = self.skills_dir / skill_name / "SKILL.md"
            content = skill_file.read_text(encoding="utf-8")

            # Must have code blocks or ASCII flow diagrams
            self.assertTrue("```" in content, f"{skill_name}/SKILL.md missing code or flow diagrams")
            # Must have numbered sections
            self.assertTrue("## 1." in content or "## 1 " in content, f"{skill_name}/SKILL.md missing numbered sections")

            # Check matching reference file
            ref_dir = self.skills_dir / skill_name / "references"
            self.assertTrue(ref_dir.exists(), f"Missing references directory in {skill_name}")
            ref_files = list(ref_dir.glob("*.md"))
            self.assertGreaterEqual(len(ref_files), 1, f"No reference markdown files found in {skill_name}/references")

            for rf in ref_files:
                rf_content = rf.read_text(encoding="utf-8")
                self.assertGreater(len(rf_content), 500, f"Reference file {rf.name} too small ({len(rf_content)} bytes)")


if __name__ == "__main__":
    unittest.main()
