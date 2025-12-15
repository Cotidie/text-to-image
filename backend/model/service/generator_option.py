from dataclasses import dataclass
from typing import Callable

@dataclass    
class GenerateParameter:
    prompt: str
    width: int = 512
    height: int = 512
    steps: int = 8

# Option type: a callable that modifies GenerateParameters
GenerateOption = Callable[[GenerateParameter], None]

def with_size(width: int, height: int) -> GenerateOption:
    def apply(params: GenerateParameter):
        params.width = width
        params.height = height
    return apply

def with_steps(steps: int) -> GenerateOption:
    def apply(params: GenerateParameter):
        params.steps = steps
    return apply