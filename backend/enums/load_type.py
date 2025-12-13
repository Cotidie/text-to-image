from enum import Enum

class LoadType(str, Enum):
    LOCAL = "local"
    REMOTE = "remote"
    NONE = "none"
