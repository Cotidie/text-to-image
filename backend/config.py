import os
from dataclasses import dataclass
from model.device import Device
from model.model import LoadType, Model, SupportedModels
from huggingface_hub import HfApi
from utils import DeviceDetector

@dataclass
class Config:
    """Configuration settings for the image generation service."""
    model: Model = None
    device: Device = None

    port: int = 5555
    home_models: str = "/app/models"
    home_cache: str = "/app/cache"

class ConfigBuilder:

    def __init__(self):
        self._config = Config()
        self._config.device = DeviceDetector.detect()

    def with_env(self) -> "ConfigBuilder":
        model_type = os.getenv("MODEL_TYPE", self._config.model.type.value).lower()
        model_path = os.getenv("MODEL_PATH", self._config.model.path)
        model_home = os.getenv("MODEL_HOME", self._config.home_models)
        home_cache = os.getenv("HF_HOME", self._config.home_cache)
        port = os.getenv("PORT", self._config.port)
        
        if model_type == LoadType.REMOTE.value:
            self.with_remote_model(model_path)
        elif model_type == LoadType.LOCAL.value:
            model_path = os.path.join(model_home, model_path)
            self.with_local_model(model_path)
        else:
            raise ValueError(f"Unsupported MODEL_TYPE: {model_type}")

        self._config.home_models = model_home    
        self._config.home_cache = home_cache
        self._config.port = port

        return self
    
    def with_model(self, model: Model) -> "ConfigBuilder":
        self._config.model = model
        return self

    def with_remote_model(self, repo: str) -> "ConfigBuilder":
        HfApi().model_info(repo)  # raises error if not found

        model = Model(
            type=LoadType.REMOTE,
            name=repo.split("/")[-1],
            path=repo
        )
        self._config.model = model
        return self
    
    def with_local_model(self, path: str) -> "ConfigBuilder":
        if not os.path.exists(path):
            raise FileNotFoundError(f"Local model path not found: {path}")

        model = Model(
            type=LoadType.LOCAL,
            name=os.path.basename(path),
            path=path
        )
        self._config.model = model

        return self
    
    def with_port(self, port: int) -> "ConfigBuilder":
        self._config.port = port
        return self

    def build(self) -> Config:
        return self._config