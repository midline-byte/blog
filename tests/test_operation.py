import tempfile
import unittest
from pathlib import Path

from src.operation import evaluate_alert_level, save_operation_result


class OperationTest(unittest.TestCase):
    def test_saves_operation_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "result.json"

            save_operation_result(path, {"status": "success"})

            self.assertTrue(path.exists())
            self.assertIn("success", path.read_text(encoding="utf-8"))

    def test_evaluates_alert_level(self):
        self.assertEqual(evaluate_alert_level(True, 0), "level0")
        self.assertEqual(evaluate_alert_level(False, 1), "level1")
        self.assertEqual(evaluate_alert_level(False, 3), "level2")
        self.assertEqual(evaluate_alert_level(False, 4), "level3")


if __name__ == "__main__":
    unittest.main()
