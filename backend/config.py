import os

from enums import Model, DeviceType

class Config:
    """Configuration settings for the image generation service."""
    
    def __init__(self):
        self.model = Model.SD_TURBO.value
        self.device_type: DeviceType = DeviceType.detect_device()
        self.port = 5555

    def load_from_env(self) -> "Config":
        """Load configuration from environment variables."""
        self.model = os.getenv("DEFAULT_MODEL", self.model)
        self.port = int(os.getenv("PORT", self.port))
        return self
