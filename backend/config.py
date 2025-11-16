import os
from enum import Enum


class Model(str, Enum):
    """Supported text-to-image model names."""
    SD_TURBO = "stabilityai/sd-turbo"
    SDXL_TURBO = "stabilityai/sdxl-turbo"


class Config:
    """Configuration settings for the image generation service."""
    
    DEFAULT_MODEL: str  = Model.SD_TURBO.value    # which SD model to use
    PORT: int           = 5555                    # port number for flask 

    @classmethod
    def load_from_env(cls) -> None:
        """Load configuration from environment variables."""
        
        cls.DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", cls.DEFAULT_MODEL)
        cls.PORT = int(os.getenv("PORT", cls.PORT))