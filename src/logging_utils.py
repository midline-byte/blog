from __future__ import annotations

import logging
from pathlib import Path


def configure_logger(log_path: str | Path = "logs/app.log") -> logging.Logger:
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("blog_ai")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(handler)

    return logger
