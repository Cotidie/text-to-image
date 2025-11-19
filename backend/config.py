import os
from dataclasses import dataclass
from model.device import Device
from utils import DeviceDetector
from enums import Model
@dataclass
class Config:
    """Configuration settings for the image generation service."""
    model: str = Model.SDXL_TURBO.value
    device: Device = None
    port: int = 5555

class ConfigBuilder:

    def __init__(self):
        self._config = Config()

    def with_env(self) -> "ConfigBuilder":
        self._config.model = os.getenv("MODEL", self._config.model)
        self._config.port = int(os.getenv("PORT", self._config.port))
        return self
    
    def with_model(self, model: Model) -> "ConfigBuilder":
        self._config.model = model.value
        return self
    
    def with_port(self, port: int) -> "ConfigBuilder":
        self._config.port = port
        return self

    def build(self) -> Config:
        self._config.device = DeviceDetector.detect()

        return self._config