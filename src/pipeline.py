from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from src.analyze_image import analyze_image
from src.blog_generator import generate_blog_post
from src.operation import audit_event
from src.publish_engine import build_post_payload, publish_post


ROOT = Path(__file__).resolve().parents[1]


def run_pipeline(
    image_path: str,
    skill_path: str | None = None,
    user_settings: dict[str, Any] | None = None,
    publish: bool = False,
) -> dict[str, Any]:
    audit_event("User Uploaded Image", {"image": image_path})
    analysis = analyze_image(image_path)
    if analysis.get("result") == "fail":
        return {"status": "fail", "stage": "image-analysis", "analysis": analysis}

    skill_file = skill_path or str(ROOT / "skills" / analysis.get("skill", "daily.md"))
    skill_markdown = Path(skill_file).read_text(encoding="utf-8")
    generated = generate_blog_post(analysis, skill_markdown, user_settings)
    audit_event("Generated Blog", {"outputPath": generated.outputPath})

    result: dict[str, Any] = {
        "status": "success",
        "analysis": analysis,
        "post": generated.to_dict(),
    }

    if publish:
        payload = build_post_payload(
            generated.title,
            generated.markdown,
            generated.hashtags,
            mode=(user_settings or {}).get("mode", "draft"),
        )
        publish_result = publish_post(payload)
        audit_event("Published Blog", publish_result.to_dict())
        result["publish"] = publish_result.to_dict()

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--publish", action="store_true")
    parser.add_argument("--mode", choices=["draft", "publish"], default="draft")
    parser.add_argument("--length", choices=["short", "medium", "long"], default="medium")
    args = parser.parse_args()

    result = run_pipeline(
        args.image,
        user_settings={"mode": args.mode, "length": args.length},
        publish=args.publish,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
