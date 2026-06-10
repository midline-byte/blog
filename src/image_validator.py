from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


SUPPORTED_EXTENSIONS = {"jpg", "jpeg", "png", "webp", "heic"}
MAX_FILE_SIZE_BYTES = 20 * 1024 * 1024


@dataclass(frozen=True)
class ImageMetadata:
    file_name: str
    extension: str
    size_bytes: int
    width: int
    height: int


class ImageValidationError(ValueError):
    pass


def validate_image_path(
    image_path: str | Path,
    supported_extensions: set[str] | None = None,
    max_file_size_bytes: int = MAX_FILE_SIZE_BYTES,
) -> ImageMetadata:
    path = Path(image_path)
    extensions = supported_extensions or SUPPORTED_EXTENSIONS

    if not path.exists():
        raise ImageValidationError(f"image file does not exist: {path}")
    if not path.is_file():
        raise ImageValidationError(f"image path is not a file: {path}")

    extension = path.suffix.lower().lstrip(".")
    if extension not in extensions:
        raise ImageValidationError(f"unsupported image extension: {extension}")

    size_bytes = path.stat().st_size
    if size_bytes > max_file_size_bytes:
        raise ImageValidationError("image file exceeds maximum size")

    width, height = read_image_dimensions(path)
    if width <= 0 or height <= 0:
        raise ImageValidationError("image dimensions could not be read")

    return ImageMetadata(
        file_name=path.name,
        extension=extension,
        size_bytes=size_bytes,
        width=width,
        height=height,
    )


def read_image_dimensions(path: Path) -> tuple[int, int]:
    extension = path.suffix.lower().lstrip(".")
    with path.open("rb") as file:
        header = file.read(64)

    if extension == "png":
        return _png_dimensions(header)
    if extension in {"jpg", "jpeg"}:
        return _jpeg_dimensions(path)
    if extension == "webp":
        return _webp_dimensions(header)
    if extension == "heic":
        return (0, 0)

    return (0, 0)


def _png_dimensions(header: bytes) -> tuple[int, int]:
    if len(header) < 24 or header[:8] != b"\x89PNG\r\n\x1a\n":
        return (0, 0)
    return (
        int.from_bytes(header[16:20], "big"),
        int.from_bytes(header[20:24], "big"),
    )


def _jpeg_dimensions(path: Path) -> tuple[int, int]:
    with path.open("rb") as file:
        if file.read(2) != b"\xff\xd8":
            return (0, 0)

        while True:
            marker_start = file.read(1)
            if not marker_start:
                return (0, 0)
            if marker_start != b"\xff":
                continue

            marker = file.read(1)
            while marker == b"\xff":
                marker = file.read(1)

            if marker in {b"\xc0", b"\xc1", b"\xc2", b"\xc3"}:
                file.read(3)
                height = int.from_bytes(file.read(2), "big")
                width = int.from_bytes(file.read(2), "big")
                return (width, height)

            segment_length_raw = file.read(2)
            if len(segment_length_raw) != 2:
                return (0, 0)
            segment_length = int.from_bytes(segment_length_raw, "big")
            if segment_length < 2:
                return (0, 0)
            file.seek(segment_length - 2, 1)


def _webp_dimensions(header: bytes) -> tuple[int, int]:
    if len(header) < 30 or header[:4] != b"RIFF" or header[8:12] != b"WEBP":
        return (0, 0)

    chunk = header[12:16]
    if chunk == b"VP8X" and len(header) >= 30:
        width = int.from_bytes(header[24:27], "little") + 1
        height = int.from_bytes(header[27:30], "little") + 1
        return (width, height)

    return (0, 0)
