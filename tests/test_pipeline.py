import tempfile
import unittest
from pathlib import Path

from src.pipeline import run_pipeline


PNG_1X1 = (
    b"\x89PNG\r\n\x1a\n"
    b"\x00\x00\x00\rIHDR"
    b"\x00\x00\x00\x01"
    b"\x00\x00\x00\x01"
    b"\x08\x02\x00\x00\x00"
    b"\x90wS\xde"
    b"\x00\x00\x00\x00IEND\xaeB`\x82"
)


class PipelineTest(unittest.TestCase):
    def test_runs_analysis_and_generation_without_publish(self):
        with tempfile.TemporaryDirectory() as tmp:
            image = Path(tmp) / "food-menu.png"
            image.write_bytes(PNG_1X1)

            result = run_pipeline(str(image), publish=False)

            self.assertEqual(result["status"], "success")
            self.assertIn("analysis", result)
            self.assertIn("post", result)


if __name__ == "__main__":
    unittest.main()
