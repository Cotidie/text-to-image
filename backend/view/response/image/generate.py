"""Image response implementations."""

import base64
from PIL import Image
from dataclasses import dataclass

from view.interface import Serializable


@dataclass
class GenerateImage(Serializable):
    """
    Data payload for image generation endpoint
    
    Attributes:
        image (Image): The generated image.
        time (float): The time taken to generate the image.
        format (str): The format of the image.
    """
    image: Image.Image
    time: float
    format: str = "PNG"

    def to_dict(self) -> dict:
        return {
            "image": base64.b64encode(self.image.tobytes()).decode('utf-8'),
            "format": self.format,
            "time": self.time,
        }