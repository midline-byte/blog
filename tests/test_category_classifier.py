import json
import unittest
from pathlib import Path

from src.category_classifier import classify_image


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class CategoryClassifierTest(unittest.TestCase):
    def test_classifies_restaurant(self):
        result = classify_image(
            {
                "objects": ["food", "plate", "table", "menu"],
                "locationType": "restaurant",
                "keywords": ["coffee"],
            },
            load_json("config/categories.json"),
            load_json("config/image-analysis.json"),
        )

        self.assertEqual(result.category, "restaurant")
        self.assertEqual(result.skill, "restaurant.md")
        self.assertFalse(result.needs_review)

    def test_falls_back_to_daily_when_confidence_is_low(self):
        result = classify_image(
            {"objects": ["wall"], "keywords": ["shadow"]},
            load_json("config/categories.json"),
            load_json("config/image-analysis.json"),
        )

        self.assertEqual(result.category, "daily")
        self.assertEqual(result.skill, "daily.md")
        self.assertTrue(result.needs_review)


if __name__ == "__main__":
    unittest.main()
