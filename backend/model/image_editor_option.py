from dataclasses import dataclass
from typing import Callable

@dataclass    
class EditParameter:
    prompt: str
    width: int = 512
    height: int = 512
    steps: int = 8
    strength: float = 0.4

EditOption = Callable[[EditParameter], None]