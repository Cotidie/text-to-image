from dataclasses import dataclass
from typing import Optional
from flask import Request
from view.interface import Validatable
from view.request.helper import parse_json_data
from PIL.Image import Image

class EditImage(Validatable):
    """Request model for image editing."""

    def __init__(self, request: Request):
        data = parse_json_data(request)
        self.image = data.get("image")
        self.prompt = data.get("prompt", "")
        self.format = data.get("format", "png")
        self.steps = int(data.get("steps", 4))
        self.strength = float(data.get("strength", 0.6))

    def validate(self) -> None:
        if not self.image:
            raise ValueError("Image data cannot be empty.")
        if not self.prompt:
            raise ValueError("Prompt cannot be empty.")
        if self.steps * self.strength < 1:
            raise ValueError("The product of steps and strength must be at least 1.")
