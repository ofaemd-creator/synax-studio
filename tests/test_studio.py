import tempfile
import unittest
from pathlib import Path
from synax.studio_app import build_macos_app_bundle

class TestSynaxStudio(unittest.TestCase):
    def test_studio_html_present(self):
        html = Path(__file__).resolve().parents[1] / "editors" / "vscode-synax" / "media" / "studio.html"
        self.assertTrue(html.exists())
        self.assertIn("SYNAX Studio IDE", html.read_text(encoding="utf-8"))

    def test_build_macos_bundle(self):
        with tempfile.TemporaryDirectory() as td:
            app = build_macos_app_bundle(Path(td) / "SYNAX Studio.app")
            self.assertTrue((app / "Contents" / "Info.plist").exists())

if __name__ == "__main__":
    unittest.main()
