from typing import Optional
from flask import Request
from view.interface import Validatable
from view.request.helper import parse_json_data

class GenerateImage(Validatable):
    """Request model for image generation."""
    
    def __init__(self, request: Request):
        data = parse_json_data(request)
        self.prompt = data.get("prompt", "")
        self.format = data.get("format", "png")
        self.width = int(data.get("width", 512))
        self.height = int(data.get("height", 512))
        self.steps = int(data.get("steps", 8))

    def validate(self) -> None:
        if not self.prompt:
            raise ValueError("Prompt cannot be empty.")
