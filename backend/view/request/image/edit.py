from dataclasses import dataclass
from typing import Optional
from flask import Request
from view.interface import Parsable, Validatable
from view.request.helper import parse_data
from PIL.Image import Image

@dataclass
class EditImage(Parsable, Validatable):
    """Request model for image editing."""
    image: Image = None
    prompt: str = ""
    format: Optional[str] = "png"
    steps: Optional[int] = 8
    strength: Optional[float] = 0.8
    
    @classmethod
    def from_request(cls, request: Request) -> 'EditImage':
        default = EditImage()
        data = parse_data(request)
        return cls(
            image=data.get("image"),
            prompt=data.get("prompt", default.prompt),
            format=data.get("format", default.format),
            steps=int(data.get("steps", default.steps)),
            strength=float(data.get("strength", default.strength))
        )

    def validate(self) -> None:
        if not self.image:
            raise ValueError("Image data cannot be empty.")
        if not self.prompt:
            raise ValueError("Prompt cannot be empty.")
