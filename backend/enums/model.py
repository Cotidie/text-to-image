from enum import Enum

class Model(str, Enum):
    """Supported text-to-image model names."""
    SD_TURBO = "stabilityai/sd-turbo"
    SDXL_TURBO = "stabilityai/sdxl-turbo"

