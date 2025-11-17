import os
from enum import Enum


class Model(str, Enum):
    """Supported text-to-image model names."""
    SD_TURBO = "stabilityai/sd-turbo"
    SDXL_TURBO = "stabilityai/sdxl-turbo"


class Config:
    """Configuration settings for the image generation service."""
    
    def __init__(self):
        self.DEFAULT_MODEL = Model.SD_TURBO.value
        self.PORT = 5555

    def load_from_env(self) -> "Config":
        """Load configuration from environment variables."""
        self.DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", self.DEFAULT_MODEL)
        self.PORT = int(os.getenv("PORT", self.PORT))
        
        return self