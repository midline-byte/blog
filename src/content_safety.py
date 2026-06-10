from __future__ import annotations

import re
from typing import Iterable


PROMPT_INJECTION_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in [
        r"ignore\s+(all\s+)?previous\s+instructions",
        r"disregard\s+(the\s+)?(system|developer|previous)\s+instructions",
        r"print\s+(the\s+)?prompt",
        r"reveal\s+(the\s+)?(system|developer)\s+prompt",
        r"you\s+are\s+now",
    ]
]


DEFAULT_BLOCKED_PHRASES = [
    "best ever",
    "guaranteed",
    "miracle",
    "100% effective",
    "limited time only",
]


def sanitize_extracted_text(values: Iterable[str]) -> list[str]:
    sanitized: list[str] = []
    for value in values:
        text = str(value or "").strip()
        if not text:
            continue
        if any(pattern.search(text) for pattern in PROMPT_INJECTION_PATTERNS):
            continue
        sanitized.append(text[:200])
    return sanitized


def remove_blocked_phrases(text: str, blocked_phrases: Iterable[str] | None = None) -> str:
    cleaned = text
    for phrase in blocked_phrases or DEFAULT_BLOCKED_PHRASES:
        cleaned = re.sub(re.escape(phrase), "", cleaned, flags=re.IGNORECASE)
    return re.sub(r"\s{2,}", " ", cleaned).strip()
