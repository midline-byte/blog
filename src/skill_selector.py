from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SkillSelection:
    skill: str
    category: str
    confidence: float
    matched_signals: list[str]
    fallback_used: bool


def _normalize(value: Any) -> str:
    return str(value or "").strip().lower()


def _analysis_terms(analysis: dict[str, Any]) -> set[str]:
    terms: set[str] = set()
    scalar_fields = ["mainSubject", "setting", "mood"]
    list_fields = ["objects", "textInImage", "categoryHints", "keywords"]

    for field in scalar_fields:
        value = _normalize(analysis.get(field))
        if value:
            terms.update(value.replace("-", " ").split())
            terms.add(value)

    for field in list_fields:
        for item in analysis.get(field, []) or []:
            value = _normalize(item)
            if value:
                terms.update(value.replace("-", " ").split())
                terms.add(value)

    return terms


def select_skill(
    analysis: dict[str, Any],
    categories_config: dict[str, Any],
    routing_config: dict[str, Any],
) -> SkillSelection:
    terms = _analysis_terms(analysis)
    categories = {item["id"]: item for item in categories_config.get("categories", [])}
    priority = routing_config.get("priority", [])
    threshold = float(routing_config.get("defaultThreshold", 0.55))

    best: SkillSelection | None = None

    for category_id in priority:
        if category_id == routing_config.get("fallbackCategory", "default"):
            continue

        category = categories.get(category_id)
        if not category:
            continue

        signals = [_normalize(signal) for signal in category.get("signals", [])]
        matched = [signal for signal in signals if signal in terms]
        confidence = len(matched) / len(signals) if signals else 0.0

        if confidence >= float(category.get("minimumConfidence", threshold)):
            return SkillSelection(
                skill=category["skill"],
                category=category_id,
                confidence=round(confidence, 4),
                matched_signals=matched,
                fallback_used=False,
            )

        if best is None or confidence > best.confidence:
            best = SkillSelection(
                skill=category.get("skill", routing_config["defaultSkill"]),
                category=category_id,
                confidence=round(confidence, 4),
                matched_signals=matched,
                fallback_used=False,
            )

    daily = categories.get("daily")
    if daily and best and best.confidence > 0:
        return SkillSelection(
            skill=daily["skill"],
            category="daily",
            confidence=best.confidence,
            matched_signals=best.matched_signals,
            fallback_used=True,
        )

    return SkillSelection(
        skill=routing_config["defaultSkill"],
        category=routing_config.get("fallbackCategory", "default"),
        confidence=0.0,
        matched_signals=[],
        fallback_used=True,
    )
