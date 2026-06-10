from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.logging_utils import get_named_logger


def audit_event(event: str, details: dict[str, Any] | None = None) -> None:
    logger = get_named_logger("audit", "logs/audit.log")
    payload = {
        "time": datetime.now(timezone.utc).isoformat(),
        "event": event,
        "details": details or {},
    }
    logger.info(json.dumps(payload, ensure_ascii=False))


def save_operation_result(path: str | Path, result: dict[str, Any]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")


def evaluate_alert_level(success: bool, retry_count: int) -> str:
    if success:
        return "level0"
    if retry_count <= 1:
        return "level1"
    if retry_count <= 3:
        return "level2"
    return "level3"
