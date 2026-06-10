from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.category_classifier import classify_image
from src.image_analysis import build_analysis_result, metadata_to_analysis_terms
from src.image_validator import ImageValidationError, validate_image_path
from src.logging_utils import configure_logger


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def analyze_image(image_path: str, observations: dict | None = None) -> dict:
    logger = configure_logger(ROOT / "logs" / "app.log")

    try:
        metadata = validate_image_path(image_path)
        source_observations = observations or metadata_to_analysis_terms(metadata)
        categories = load_json("config/categories.json")
        image_config = load_json("config/image-analysis.json")
        classification = classify_image(source_observations, categories, image_config)
        result = build_analysis_result(
            image_path,
            source_observations,
            classification.to_dict(),
        )
        logger.info("image analyzed")
        return result.to_dict()
    except ImageValidationError as exc:
        logger.error("image analysis failed")
        return {"result": "fail", "message": str(exc)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--observations-json", default="")
    args = parser.parse_args()

    observations = json.loads(args.observations_json) if args.observations_json else None
    print(json.dumps(analyze_image(args.image, observations), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
