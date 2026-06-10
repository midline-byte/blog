import tempfile
import unittest
from pathlib import Path

from src.image_validator import ImageValidationError, validate_image_path


PNG_1X1 = (
    b"\x89PNG\r\n\x1a\n"
    b"\x00\x00\x00\rIHDR"
    b"\x00\x00\x00\x01"
    b"\x00\x00\x00\x01"
    b"\x08\x02\x00\x00\x00"
    b"\x90wS\xde"
    b"\x00\x00\x00\x00IEND\xaeB`\x82"
)


class ImageValidatorTest(unittest.TestCase):
    def test_validates_png_dimensions(self):
        with tempfile.TemporaryDirectory() as tmp:
            image = Path(tmp) / "food.png"
            image.write_bytes(PNG_1X1)

            metadata = validate_image_path(image)

            self.assertEqual(metadata.width, 1)
            self.assertEqual(metadata.height, 1)
            self.assertEqual(metadata.extension, "png")

    def test_rejects_unsupported_extension(self):
        with tempfile.TemporaryDirectory() as tmp:
            image = Path(tmp) / "note.txt"
            image.write_text("not an image", encoding="utf-8")

            with self.assertRaises(ImageValidationError):
                validate_image_path(image)


if __name__ == "__main__":
    unittest.main()
