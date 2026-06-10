import tempfile
import unittest
from pathlib import Path

from src.blog_generator import generate_blog_post


class BlogGeneratorTest(unittest.TestCase):
    def test_generates_markdown_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = generate_blog_post(
                {
                    "category": "restaurant",
                    "objects": ["food", "plate", "table"],
                    "ocr": ["menu"],
                    "keywords": ["pasta", "restaurant", "dinner"],
                    "locationType": "restaurant",
                    "mood": "cozy",
                },
                "# Restaurant Skill\n\nUse this skill for restaurant posts.",
                {"length": "short"},
                output_dir=tmp,
            )

            self.assertGreaterEqual(len(result.titleCandidates), 5)
            self.assertGreaterEqual(len(result.seoKeywords), 5)
            self.assertGreaterEqual(len(result.hashtags), 10)
            self.assertTrue(Path(result.outputPath).exists())
            self.assertIn("# ", result.markdown)


if __name__ == "__main__":
    unittest.main()
