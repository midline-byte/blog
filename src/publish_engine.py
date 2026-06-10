from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from src.logging_utils import get_named_logger


@dataclass(frozen=True)
class PublishResult:
    status: str
    postId: str = ""
    url: str = ""
    message: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "status": self.status,
            "postId": self.postId,
            "url": self.url,
            "message": self.message,
        }


def build_post_payload(title: str, content: str, tags: list[str], mode: str = "draft") -> dict[str, Any]:
    if mode not in {"draft", "publish"}:
        raise ValueError("mode must be draft or publish")
    return {
        "title": title,
        "content": content,
        "tags": tags,
        "status": mode,
    }


def publish_post(payload: dict[str, Any], max_attempts: int = 3) -> PublishResult:
    upload_logger = get_named_logger("upload", "logs/upload.log")
    error_logger = get_named_logger("error", "logs/error.log")
    api_url = os.getenv("BLOG_API_URL", "")
    token = os.getenv("BLOG_API_TOKEN", "")

    if not api_url or not token:
        result = PublishResult(status="fail", message="BLOG_API_URL or BLOG_API_TOKEN is not configured")
        error_logger.error(result.message)
        return result

    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        api_url,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    last_error = ""
    for attempt in range(1, max_attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                data = json.loads(response.read().decode("utf-8") or "{}")
            result = PublishResult(
                status="success",
                postId=str(data.get("postId") or data.get("id") or ""),
                url=str(data.get("url") or ""),
            )
            upload_logger.info("Blog Published Post ID: %s", result.postId)
            return result
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last_error = str(exc)
            error_logger.error("Publish attempt %s failed: %s", attempt, last_error)
            if attempt < max_attempts:
                time.sleep(1)

    return PublishResult(status="fail", message=last_error or "API Error")
