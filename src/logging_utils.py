from __future__ import annotations

import logging
from pathlib import Path


def configure_logger(log_path: str | Path = "logs/app.log") -> logging.Logger:
    return get_named_logger("blog_ai", log_path)


def get_named_logger(name: str, log_path: str | Path) -> logging.Logger:
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    for existing_handler in logger.handlers[:]:
        logger.removeHandler(existing_handler)
        existing_handler.close()

    handler = logging.FileHandler(path, encoding="utf-8")
    handler.setFormatter(logging.Formatter("[%(levelname)s] %(message)s"))
    logger.addHandler(handler)

    return logger
