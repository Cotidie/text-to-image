"""Image response implementations."""

import base64
from PIL import Image
from dataclasses import dataclass

from model.interface import Jsonifiable


@dataclass
class GenerateImage(Jsonifiable):
    """Data container for image information."""
    image: Image.Image
    format: str = "PNG"

    def to_dict(self) -> dict:
        return {
            "image": base64.b64encode(self.image.tobytes()).decode('utf-8'),
            "format": self.format,
            "size": self.image.size,
            "mode": self.image.mode
        }