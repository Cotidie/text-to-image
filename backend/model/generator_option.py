from dataclasses import dataclass
from typing import Callable

@dataclass    
class GenerateParameters:
    prompt: str
    width: int = 512
    height: int = 512
    steps: int = 8
    strength: float = 0.8

# Option type: a callable that modifies GenerateParameters
GenerateOption = Callable[[GenerateParameters], None]

def with_size(width: int, height: int) -> GenerateOption:
    def apply(params: GenerateParameters):
        params.width = width
        params.height = height
    return apply

def with_steps(steps: int) -> GenerateOption:
    def apply(params: GenerateParameters):
        params.steps = steps
    return apply

def with_strength(strength: float) -> GenerateOption:
    def apply(params: GenerateParameters):
        params.strength = strength
    return apply