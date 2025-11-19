import os
from dataclasses import dataclass
from model.device import Device
from enums import Model
@dataclass
class Config:
    """Configuration settings for the image generation service."""
    
    def __init__(self):
        self.model = Model.SD_TURBO.value
        self.port = 5555
        self.device: Device = None

    def load_from_env(self) -> "Config":
        """Load configuration from environment variables."""
        self.model = os.getenv("DEFAULT_MODEL", self.model)
        self.port = int(os.getenv("PORT", self.port))
        return self
