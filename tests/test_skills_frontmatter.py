"""
Suite 2: Skill Directory & YAML Frontmatter Schema Validation.
Validates that every skill directory under skills/ contains SKILL.md with valid YAML frontmatter,
matching folder name, third-person trigger description, and structured body content.
"""
import re
import unittest
from pathlib import Path

try:
    from conftest import PLUGIN_ROOT, parse_yaml_frontmatter
except ImportError:
    from .conftest import PLUGIN_ROOT, parse_yaml_frontmatter


class TestSkillsFrontmatter(unittest.TestCase):
    """Tier 2: Skills directory layout, frontmatter, and progressive disclosure tests."""

    @classmethod
    def setUpClass(cls):
        cls.skills_dir = PLUGIN_ROOT / "skills"
        cls.skill_dirs = []
        if cls.skills_dir.exists():
            cls.skill_dirs = [
                d for d in cls.skills_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
            ]

    def test_skills_directory_exists_and_populated(self):
        """Validates that skills/ directory exists and contains skill packages."""
        self.assertTrue(
            self.skills_dir.exists(), f"Skills directory not found at {self.skills_dir}"
        )
        self.assertTrue(
            len(self.skill_dirs) > 0,
            f"No skill subdirectories found in {self.skills_dir}",
        )

    def test_all_skills_have_valid_skill_md(self):
        """Validates that every skill subdirectory contains a non-empty SKILL.md file."""
        for skill_dir in self.skill_dirs:
            with self.subTest(skill=skill_dir.name):
                skill_file = skill_dir / "SKILL.md"
                self.assertTrue(
                    skill_file.exists(),
                    f"Missing SKILL.md in skill directory: {skill_dir.name}",
                )
                content = skill_file.read_text(encoding="utf-8").strip()
                self.assertTrue(
                    len(content) > 50,
                    f"SKILL.md in {skill_dir.name} is too short ({len(content)} chars)",
                )

    def test_all_skills_yaml_frontmatter_schema(self):
        """Validates YAML frontmatter parsing, 'name' and 'description' fields, and naming invariants."""
        name_regex = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

        for skill_dir in self.skill_dirs:
            with self.subTest(skill=skill_dir.name):
                skill_file = skill_dir / "SKILL.md"
                content = skill_file.read_text(encoding="utf-8")

                fm, body = parse_yaml_frontmatter(content)
                self.assertIsNotNone(
                    fm,
                    f"Failed to parse YAML frontmatter in {skill_dir.name}/SKILL.md. Must start with ---",
                )

                # Validate 'name'
                self.assertIn(
                    "name",
                    fm,
                    f"Missing 'name' in frontmatter of {skill_dir.name}/SKILL.md",
                )
                skill_name = fm["name"]
                self.assertTrue(
                    name_regex.match(skill_name),
                    f"Skill name '{skill_name}' in {skill_dir.name} must be lowercase-hyphenated (e.g. 'my-skill-name')",
                )
                self.assertEqual(
                    skill_name,
                    skill_dir.name,
                    f"Skill frontmatter name '{skill_name}' does not match folder name '{skill_dir.name}'",
                )

                # Validate 'description'
                self.assertIn(
                    "description",
                    fm,
                    f"Missing 'description' in frontmatter of {skill_dir.name}/SKILL.md",
                )
                desc = fm["description"]
                self.assertIsInstance(
                    desc,
                    str,
                    f"'description' in {skill_dir.name}/SKILL.md must be a string",
                )
                self.assertTrue(
                    len(desc.strip()) >= 20,
                    f"Description in {skill_dir.name}/SKILL.md is too short ({len(desc)} chars). Must be descriptive trigger.",
                )

                # Progressive disclosure: third-person phrasing check
                # Should not start with "I " or "We " or "My "
                first_words = desc.strip().split()
                if first_words:
                    self.assertNotIn(
                        first_words[0].lower(),
                        ["i", "we", "my", "our"],
                        f"Description in {skill_dir.name}/SKILL.md should use third-person phrasing, not first-person ('{first_words[0]}')",
                    )

                # Body validation: must have substantive content and headings
                self.assertTrue(
                    len(body.strip()) > 50,
                    f"Body content of {skill_dir.name}/SKILL.md is too short after frontmatter",
                )
                self.assertTrue(
                    "#" in body,
                    f"Body of {skill_dir.name}/SKILL.md should contain structured markdown headings",
                )

    def test_skill_references_and_scripts_are_valid(self):
        """Validates that any files in references/ or scripts/ subdirectories are non-empty."""
        for skill_dir in self.skill_dirs:
            refs_dir = skill_dir / "references"
            if refs_dir.exists() and refs_dir.is_dir():
                for ref_file in refs_dir.iterdir():
                    if ref_file.is_file() and not ref_file.name.startswith("."):
                        with self.subTest(skill=skill_dir.name, ref=ref_file.name):
                            self.assertTrue(
                                ref_file.stat().st_size > 0,
                                f"Reference file {ref_file} is empty (0 bytes)",
                            )

            scripts_dir = skill_dir / "scripts"
            if scripts_dir.exists() and scripts_dir.is_dir():
                for script_file in scripts_dir.iterdir():
                    if script_file.is_file() and not script_file.name.startswith("."):
                        with self.subTest(skill=skill_dir.name, script=script_file.name):
                            self.assertTrue(
                                script_file.stat().st_size > 0,
                                f"Script file {script_file} is empty (0 bytes)",
                            )


if __name__ == "__main__":
    unittest.main()
