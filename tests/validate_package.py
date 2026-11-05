"""Validate the shareable package with Python's standard library.

This checks packaging, not PPT quality or real-world model behavior.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "changxin-ppt-standard"
ALLOWED = {
    ".gitignore", "LICENSE", "README.md", "VERSION",
    "tests/validate_package.py",
    "skills/changxin-ppt-standard/SKILL.md",
    "skills/changxin-ppt-standard/agents/openai.yaml",
    "skills/changxin-ppt-standard/references/visual-standard.md",
    "skills/changxin-ppt-standard/references/content-patterns.md",
    "skills/changxin-ppt-standard/references/delivery-checklist.md",
}


def public_files():
    return [p for p in ROOT.rglob("*") if p.is_file()
            and ".git" not in p.relative_to(ROOT).parts
            and "__pycache__" not in p.relative_to(ROOT).parts]


class PackageTests(unittest.TestCase):
    def test_allowlist(self):
        self.assertEqual({p.relative_to(ROOT).as_posix() for p in public_files()}, ALLOWED)

    def test_encoding_and_scaffolding(self):
        for p in public_files():
            with self.subTest(file=p.relative_to(ROOT)):
                text = p.read_text(encoding="utf-8")
                self.assertNotIn("\ufffd", text)
                if p.suffix in {".md", ".yaml"}:
                    self.assertNotIn("[TODO:", text)
                self.assertNotIn("\x00", text)

    def test_entrypoint(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        front = text.split("---", 2)[1]
        self.assertRegex(front, r"(?m)^name: changxin-ppt-standard$")
        self.assertRegex(front, r'(?m)^description: ".+"$')
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f'version: "{version}"', front)
        self.assertIn(f"版本：{version}", (ROOT / "README.md").read_text(encoding="utf-8"))

    def test_ui_metadata(self):
        text = (SKILL / "agents/openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "长信科技PPT规范"', text)
        self.assertIn("$changxin-ppt-standard", text)
        self.assertIn("allow_implicit_invocation: true", text)

    def test_local_links(self):
        for p in public_files():
            if p.suffix != ".md":
                continue
            for dest in re.findall(r"\]\(([^)]+)\)", p.read_text(encoding="utf-8")):
                if "://" in dest or dest.startswith("#"):
                    continue
                resolved = (p.parent / dest.split("#", 1)[0]).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT.resolve()), dest)
                self.assertTrue(resolved.is_file(), dest)

    def test_no_local_source_paths_or_credentials(self):
        patterns = [r"[A-Za-z]:[\\/]Users[\\/]", r"wxid_[a-zA-Z0-9_]+",
                    r"gh[pousr]_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}"]
        for p in public_files():
            text = p.read_text(encoding="utf-8")
            for pattern in patterns:
                self.assertIsNone(re.search(pattern, text), str(p.relative_to(ROOT)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
