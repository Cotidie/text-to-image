from enum import Enum


class Model(str, Enum):
    """Supported text-to-image model names."""
    SD_TURBO = "stabilityai/sd-turbo"
    SDXL_TURBO = "stabilityai/sdxl-turbo"


class Config:
    """Configuration settings for the image generation service."""
    
    DEFAULT_MODEL: str  = Model.SD_TURBO.value    # which SD model to use
    PORT: int   = 5006                    # port number for flask 