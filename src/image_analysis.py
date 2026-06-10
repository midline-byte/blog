from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from src.image_validator import ImageMetadata, validate_image_path
from src.content_safety import sanitize_extracted_text


@dataclass
class ImageAnalysisResult:
    fileName: str
    width: int
    height: int
    objects: list[str] = field(default_factory=list)
    ocr: list[str] = field(default_factory=list)
    locationType: str = ""
    mood: str = ""
    dominantColors: list[str] = field(default_factory=list)
    keywords: list[str] = field(default_factory=list)
    category: str = ""
    confidence: int = 0
    skill: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def build_analysis_result(
    image_path: str | Path,
    observations: dict[str, Any] | None,
    category_result: dict[str, Any],
) -> ImageAnalysisResult:
    metadata = validate_image_path(image_path)
    data = observations or {}

    return ImageAnalysisResult(
        fileName=metadata.file_name,
        width=metadata.width,
        height=metadata.height,
        objects=_list(data.get("objects")),
        ocr=sanitize_extracted_text(_list(data.get("ocr") or data.get("textInImage"))),
        locationType=str(data.get("locationType") or data.get("location_type") or ""),
        mood=str(data.get("mood") or ""),
        dominantColors=_list(data.get("dominantColors") or data.get("dominant_colors")),
        keywords=sanitize_extracted_text(_list(data.get("keywords"))),
        category=str(category_result.get("category", "")),
        confidence=int(category_result.get("confidence", 0)),
        skill=str(category_result.get("skill", "")),
    )


def metadata_to_analysis_terms(metadata: ImageMetadata) -> dict[str, Any]:
    stem_terms = metadata.file_name.rsplit(".", 1)[0].replace("-", " ").replace("_", " ")
    return {
        "objects": [],
        "ocr": [],
        "keywords": stem_terms.split(),
    }


def _list(value: Any) -> list[str]:
    if not value:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)]
