from dataclasses import dataclass
from enum import Enum

class LoadType(str, Enum):
    LOCAL = "local"
    REMOTE = "remote"

@dataclass
class Model:
    type: LoadType
    path: str
    name: str = ""

class SupportedModels:
    SD_TURBO = Model(
        type=LoadType.REMOTE,
        name="sd-turbo",
        path="stabilityai/sd-turbo"
    )
    SDXL_TURBO = Model(
        type=LoadType.REMOTE,
        name="sdxl-turbo",
        path="stabilityai/sdxl-turbo"
    )