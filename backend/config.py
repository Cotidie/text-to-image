import os
from dataclasses import dataclass
from model.device import Device
from model.model import LoadType, Model
from huggingface_hub import HfApi
from utils import DeviceDetector

@dataclass
class Config:
    """Configuration settings for the image generation service."""
    model: Model
    device: Device

    port: int = 5555

class ConfigBuilder:

    def __init__(self):
        # Builder elements should be raw values rather than dataclass-wrapped.
        # This makes it easier to override them using environment variables.
        self.load_type = LoadType.NONE
        self.model_name = "local model"
        self.model_path = ""
        self.model_repo = ""
        self.port = 5555
        self.device = DeviceDetector.detect()

    def with_env(self) -> "ConfigBuilder":
        model_type = os.getenv("LOAD_TYPE", self.load_type.value)
        model_path = os.getenv("MODEL_PATH", self.model_path)
        model_name = os.getenv("MODEL_NAME", self.model_name)
        model_repo = os.getenv("MODEL_REPO", self.model_repo)
        port = os.getenv("PORT", self.port)
        
        model_type = model_type.lower()
        if model_type == LoadType.REMOTE.value:
            self.with_remote_model(model_repo)
        elif model_type == LoadType.LOCAL.value:
            self.with_local_model(model_path)
    
        self.port = int(port)
        self.model_name = model_name

        return self
    
    def with_model(self, model: Model) -> "ConfigBuilder":
        self._config.model = model
        return self

    def with_remote_model(self, repo: str) -> "ConfigBuilder":
        HfApi().model_info(repo)  # raises error if not found

        self.load_type = LoadType.REMOTE
        self.model_path = repo
        self.model_name = repo.split("/")[-1]

        return self
    
    def with_local_model(self, path: str) -> "ConfigBuilder":
        if not os.path.exists(path):
            raise FileNotFoundError(f"Local model path not found: {path}")

        self.load_type = LoadType.LOCAL
        self.model_path = path

        return self
    
    def with_port(self, port: int) -> "ConfigBuilder":
        self.port = port
        return self

    def build(self) -> Config:
        if self.load_type == LoadType.NONE:
            raise ValueError("Model type must be specified before building Config.")

        return Config(
            model=Model(
                type=self.load_type,
                path=self.model_path,
                name=self.model_name
            ),
            device=self.device,
            port=self.port
        )