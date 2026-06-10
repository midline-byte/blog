import json
import unittest
from pathlib import Path

from src.skill_selector import select_skill


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


class SkillSelectorTest(unittest.TestCase):
    def test_selects_restaurant_by_priority(self):
        categories = load_json("config/categories.json")
        routing = load_json("config/skill-routing.json")
        analysis = {
            "mainSubject": "restaurant table",
            "objects": ["plate", "menu", "dish"],
            "categoryHints": ["travel"],
            "keywords": ["food", "cafe"],
        }

        result = select_skill(analysis, categories, routing)

        self.assertEqual(result.skill, "restaurant.md")
        self.assertEqual(result.category, "restaurant")
        self.assertFalse(result.fallback_used)

    def test_uses_default_when_no_signals_match(self):
        categories = load_json("config/categories.json")
        routing = load_json("config/skill-routing.json")
        analysis = {
            "mainSubject": "abstract shadows",
            "objects": ["wall"],
            "categoryHints": [],
            "keywords": [],
        }

        result = select_skill(analysis, categories, routing)

        self.assertEqual(result.skill, "default.md")
        self.assertTrue(result.fallback_used)


if __name__ == "__main__":
    unittest.main()
