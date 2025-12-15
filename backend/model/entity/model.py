from dataclasses import dataclass
from enum import Enum
from enums.load_type import LoadType

@dataclass
class Model:
    type: LoadType
    name: str = ""
    path: str = ""