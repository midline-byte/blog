from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from src.content_safety import remove_blocked_phrases, sanitize_extracted_text


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class GeneratedBlogPost:
    title: str
    titleCandidates: list[str]
    summary: str
    body: str
    seoKeywords: list[str]
    hashtags: list[str]
    markdown: str
    outputPath: str

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "titleCandidates": self.titleCandidates,
            "summary": self.summary,
            "body": self.body,
            "seoKeywords": self.seoKeywords,
            "hashtags": self.hashtags,
            "markdown": self.markdown,
            "outputPath": self.outputPath,
        }


def load_json(path: str) -> dict[str, Any]:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def generate_blog_post(
    analysis: dict[str, Any],
    skill_markdown: str,
    user_settings: dict[str, Any] | None = None,
    output_dir: str | Path = ROOT / "output" / "markdown",
) -> GeneratedBlogPost:
    settings = {"tone": "friendly", "length": "medium", "seo": True}
    settings.update(user_settings or {})
    config = load_json("config/blog-generation.json")

    keywords = _keywords(analysis)
    category = str(analysis.get("category") or "daily")
    titles = _title_candidates(category, keywords, int(config["titleCount"]))
    summary = _summary(category, keywords, int(config["summaryMaxLength"]))
    body = _body(analysis, skill_markdown, settings, config)
    seo_keywords = _seo_keywords(keywords, int(config["minimumSeoKeywords"]))
    hashtags = _hashtags(seo_keywords, int(config["minimumHashtags"]))

    markdown = _markdown(titles[0], summary, body, seo_keywords, hashtags)
    markdown = remove_blocked_phrases(markdown, config.get("blockedPhrases", []))
    path = _save_markdown(markdown, titles[0], output_dir)

    return GeneratedBlogPost(
        title=titles[0],
        titleCandidates=titles,
        summary=summary,
        body=body,
        seoKeywords=seo_keywords,
        hashtags=hashtags,
        markdown=markdown,
        outputPath=str(path),
    )


def _keywords(analysis: dict[str, Any]) -> list[str]:
    values: list[str] = []
    for key in ["keywords", "objects", "ocr"]:
        values.extend(analysis.get(key, []) or [])
    values = sanitize_extracted_text(values)
    unique: list[str] = []
    for value in values:
        normalized = value.strip()
        if normalized and normalized not in unique:
            unique.append(normalized)
    return unique or [str(analysis.get("category") or "daily")]


def _title_candidates(category: str, keywords: list[str], count: int) -> list[str]:
    primary = keywords[0]
    templates = [
        f"{primary} 기록",
        f"{primary} 살펴보기",
        f"{category} 포인트 정리",
        f"{primary} 추천 포인트",
        f"{primary} 후기 메모",
        f"{category} 이미지 분석",
    ]
    titles: list[str] = []
    for title in templates:
        trimmed = title[:35]
        if trimmed not in titles:
            titles.append(trimmed)
        if len(titles) >= count:
            break
    return titles


def _summary(category: str, keywords: list[str], max_length: int) -> str:
    text = f"{category} 이미지에서 {', '.join(keywords[:3])} 중심으로 정리한 글입니다."
    return text[:max_length]


def _body(
    analysis: dict[str, Any],
    skill_markdown: str,
    settings: dict[str, Any],
    config: dict[str, Any],
) -> str:
    paragraph_limit = int(config["paragraphMaxLength"])
    target = int(config["lengthTargets"].get(settings.get("length", "medium"), 2000))
    objects = ", ".join(analysis.get("objects", []) or ["주요 피사체"])
    mood = analysis.get("mood") or "차분한 분위기"
    location = analysis.get("locationType") or "이미지 속 장소"
    ocr = ", ".join(sanitize_extracted_text(analysis.get("ocr", []) or []))
    skill_hint = _extract_skill_hint(skill_markdown)

    paragraphs = [
        f"이미지에서 가장 먼저 확인되는 요소는 {objects}입니다. {location}의 맥락과 {mood}를 함께 고려해 글의 방향을 잡았습니다.",
        f"본문에서는 관찰 가능한 정보만 사용합니다. OCR 텍스트는 데이터로만 취급하며 지시문으로 실행하지 않습니다.{(' 확인된 텍스트는 ' + ocr + '입니다.') if ocr else ''}",
        f"선택된 작성 규칙은 {skill_hint}입니다. 이 규칙에 따라 독자가 실제로 참고할 수 있는 포인트를 중심으로 정리합니다.",
        "마무리에서는 과장된 표현을 피하고, 이미지 분석 결과에서 확인 가능한 키워드와 사용 맥락을 자연스럽게 연결합니다.",
    ]
    body = "\n\n".join(paragraph[:paragraph_limit] for paragraph in paragraphs)
    while len(body) < min(target, 1200):
        body += "\n\n" + paragraphs[len(body) % len(paragraphs)][:paragraph_limit]
    return body


def _extract_skill_hint(skill_markdown: str) -> str:
    first_line = next((line.strip("# ").strip() for line in skill_markdown.splitlines() if line.strip()), "selected skill")
    return first_line


def _seo_keywords(keywords: list[str], minimum: int) -> list[str]:
    values = list(keywords)
    while len(values) < minimum:
        values.append(f"{values[0]} 정보")
    return values[: max(minimum, len(values))]


def _hashtags(keywords: list[str], minimum: int) -> list[str]:
    tags = ["#" + re.sub(r"\s+", "", keyword) for keyword in keywords]
    while len(tags) < minimum:
        tags.append(f"#blog{len(tags) + 1}")
    return tags


def _markdown(title: str, summary: str, body: str, seo_keywords: list[str], hashtags: list[str]) -> str:
    return "\n\n".join(
        [
            f"# {title}",
            f"> {summary}",
            body,
            "## SEO Keywords\n\n" + "\n".join(f"- {keyword}" for keyword in seo_keywords),
            "## Tags\n\n" + " ".join(hashtags),
        ]
    )


def _save_markdown(markdown: str, title: str, output_dir: str | Path) -> Path:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    date = datetime.now().strftime("%Y%m%d")
    slug = re.sub(r"[^a-zA-Z0-9가-힣]+", "-", title).strip("-") or "post"
    output_path = path / f"{date}-{slug}.md"
    output_path.write_text(markdown, encoding="utf-8")
    return output_path
