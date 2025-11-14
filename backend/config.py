from dataclasses import dataclass


@dataclass
class Config:
    """Configuration settings for the image generation service."""
    
    model: str = "stabilityai/sd-turbo"
    default_width: int = 512
    default_height: int = 512
    default_steps: int = 30
    default_samples: int = 1
    timeout: int = 120
