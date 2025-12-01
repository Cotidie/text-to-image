from dataclasses import dataclass
from enum import Enum

class LoadType(str, Enum):
    LOCAL = "local"
    REMOTE = "remote"
    NONE = "none"

@dataclass
class Model:
    type: LoadType
    name: str = ""
    path: str = ""