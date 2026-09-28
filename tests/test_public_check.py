from pathlib import Path
import shutil
import tempfile
import unittest

from tools.check_public import ROOT, check, inventory


class PublicCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for name in inventory(ROOT):
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def tearDown(self):
        self.temp.cleanup()

    def test_clean_package_passes(self):
        self.assertEqual(check(self.root), [])

    def test_unlisted_private_file_fails(self):
        (self.root / "operator-notes.txt").write_text("synthetic notes")
        self.assertTrue(any("unexpected file" in e for e in check(self.root)))

    def test_credential_shape_is_flagged_without_echoing_it(self):
        fixture = "gh" + "p_" + "Z" * 40
        (self.root / "README.md").write_text(fixture)
        errors = check(self.root)
        self.assertTrue(any("GitHub credential" in e for e in errors))
        self.assertTrue(all(fixture not in e for e in errors))

    def test_private_path_and_broken_link_are_flagged(self):
        private_path = "/" + "root" + "/synthetic-internal-file"
        (self.root / "README.md").write_text("[internal](" + private_path + ")")
        errors = check(self.root)
        self.assertTrue(any("private operational path" in e for e in errors))
        self.assertTrue(any("non-local package link" in e for e in errors))

    def test_symlink_cannot_import_external_files(self):
        target = self.root / "README.md"
        target.unlink()
        target.symlink_to(ROOT / "README.md")
        self.assertTrue(any("symlink not allowed" in e for e in check(self.root)))

    def test_manifest_cannot_escape_package(self):
        with (self.root / "PUBLIC_FILES.txt").open("a") as file:
            file.write("../outside.txt\n")
        self.assertTrue(any("invalid public file entry" in e for e in check(self.root)))


if __name__ == "__main__":
    unittest.main()
