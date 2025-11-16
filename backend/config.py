from dataclasses import dataclass
from enum import Enum


class Model(str, Enum):
    """Supported text-to-image model names."""
    SD_TURBO = "stabilityai/sd-turbo"
    SDXL_TURBO = "stabilityai/sdxl-turbo"


class Config:
    """Configuration settings for the image generation service."""
    
    model: str = Model.SD_TURBO.value
    default_width: int = 512
    default_height: int = 512
    default_steps: int = 30
    timeout: int = 120