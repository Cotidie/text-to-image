"""Image response implementations."""

import base64
import io
from PIL import Image
from dataclasses import dataclass

from view.interface import Serializable


@dataclass
class GenerateImageResponse(Serializable):
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
        buffered = io.BytesIO()
        self.image.save(buffered, format=self.format)
        return {
            "image": base64.b64encode(buffered.getvalue()).decode('utf-8'),
            "format": self.format,
            "time": self.time,
        }