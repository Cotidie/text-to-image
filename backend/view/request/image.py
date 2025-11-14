"""Request models for image generation."""
from dataclasses import dataclass
from typing import Optional
from view.interface import Parsable, Validatable


@dataclass
class GenerateImage(Parsable, Validatable):
    """Request model for image generation."""
    prompt: str = ""
    width: Optional[int] = 512
    height: Optional[int] = 512
    steps: Optional[int] = 8
    
    def from_dict(self, data: dict) -> None:
        """
        Parse GenerateImage from JSON data.
        
        Args:
            data: JSON data as string
        """
        self.prompt = data.get("prompt", "")
        self.width = data.get("width", self.width)
        self.height = data.get("height", self.height)
        self.steps = data.get("steps", self.steps)

    def validate(self) -> None:
        if not self.prompt:
            raise ValueError("Prompt cannot be empty.")