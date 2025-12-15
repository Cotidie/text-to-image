from dataclasses import dataclass
from typing import Optional
from flask import Request
from view.interface import Validatable
from view.request.helper import parse_json_data
import PIL.Image as Image
import base64
import io

class EditImageRequest(Validatable):
    """Request model for image editing."""
    def __init__(self, request: Request):
        data = parse_json_data(request)
        self.raw_image: str = data.get("image", None)
        self.image = Image.open(io.BytesIO(base64.b64decode(self.raw_image)))
        self.prompt: str = data.get("prompt", "")
        self.format: str = data.get("format", "png")
        self.steps: int = int(data.get("steps", 4))
        self.strength: float = float(data.get("strength", 0.6))
        
        self.validate()

    def validate(self) -> None:
        if not self.raw_image:
            raise ValueError("Image data cannot be empty.")
        if not self.prompt:
            raise ValueError("Prompt cannot be empty.")
        if self.steps * self.strength < 1:
            raise ValueError("The product of steps and strength must be at least 1.")
