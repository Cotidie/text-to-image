from dataclasses import dataclass
from typing import Optional
from flask import Request
from view.interface import Parsable, Validatable
from view.request.helper import parse_data

@dataclass
class GenerateImage(Parsable, Validatable):
    """Request model for image generation."""
    prompt: str = ""
    format: Optional[str] = "png"
    width: Optional[int] = 512
    height: Optional[int] = 512
    steps: Optional[int] = 8
    
    @classmethod
    def from_request(cls, request: Request) -> 'GenerateImage':
        default = GenerateImage()
        data = parse_data(request)
        return cls(
            prompt=data.get("prompt", default.prompt),
            format=data.get("format", default.format),
            width=int(data.get("width", default.width)),
            height=int(data.get("height", default.height)),
            steps=int(data.get("steps", default.steps))
        )

    def validate(self) -> None:
        if not self.prompt:
            raise ValueError("Prompt cannot be empty.")
