from dataclasses import dataclass
from typing import Callable

@dataclass    
class EditParameter:
    prompt: str
    width: int = 512
    height: int = 512
    steps: int = 4
    strength: float = 0.6

EditOption = Callable[[EditParameter], None]

def with_strength(strength: float) -> EditOption:
    def option(param: EditParameter) -> None:
        param.strength = strength
    return option

def with_steps(steps: int) -> EditOption:
    def option(param: EditParameter) -> None:
        param.steps = steps
    return option