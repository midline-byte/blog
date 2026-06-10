from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from src.content_safety import sanitize_extracted_text


@dataclass(frozen=True)
class CategoryClassification:
    category: str
    confidence: int
    keywords: list[str]
    skill: str
    needs_review: bool
    matched_signals: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "category": self.category,
            "confidence": self.confidence,
            "keywords": self.keywords,
            "skill": self.skill,
            "needsReview": self.needs_review,
            "matchedSignals": self.matched_signals,
        }


def classify_image(
    analysis: dict[str, Any],
    categories_config: dict[str, Any],
    image_analysis_config: dict[str, Any],
) -> CategoryClassification:
    terms = _collect_terms(analysis)
    category_rules = image_analysis_config.get("categoryRules", {})
    categories = {item["id"]: item for item in categories_config.get("categories", [])}
    thresholds = image_analysis_config.get("confidence", {})
    review_threshold = int(thresholds.get("needsReviewBelow", 70))

    best_category = "daily"
    best_confidence = 0
    best_matches: list[str] = []

    for category_id, signals in category_rules.items():
        normalized_signals = [_normalize(signal) for signal in signals]
        matched = [signal for signal in normalized_signals if signal in terms]
        confidence = _confidence(len(matched), len(normalized_signals))

        if confidence > best_confidence:
            best_category = category_id
            best_confidence = confidence
            best_matches = matched

    if best_confidence < review_threshold:
        best_category = "daily"

    category = categories.get(best_category, {})
    skill = category.get("skill", "daily.md" if best_category == "daily" else "default.md")

    return CategoryClassification(
        category=best_category,
        confidence=best_confidence,
        keywords=sorted(terms),
        skill=skill,
        needs_review=best_confidence < review_threshold,
        matched_signals=best_matches,
    )


def _collect_terms(analysis: dict[str, Any]) -> set[str]:
    fields = [
        "objects",
        "ocr",
        "textInImage",
        "keywords",
        "categoryHints",
        "locationType",
        "location_type",
        "mood",
        "mainSubject",
    ]
    terms: set[str] = set()

    for field in fields:
        value = analysis.get(field)
        values = value if isinstance(value, list) else [value]
        if field in {"ocr", "textInImage"}:
            values = sanitize_extracted_text(values)
        for item in values:
            normalized = _normalize(item)
            if not normalized:
                continue
            terms.add(normalized)
            terms.update(normalized.replace("-", " ").replace("_", " ").split())

    return terms


def _normalize(value: Any) -> str:
    return str(value or "").strip().lower()


def _confidence(matches: int, signal_count: int) -> int:
    if signal_count == 0:
        return 0
    if matches == 0:
        return 0
    return min(100, int(round((matches / signal_count) * 100)))
