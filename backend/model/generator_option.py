from dataclasses import dataclass
from typing import Callable
from config import Config

@dataclass    
class GenerateParameters:
    prompt: str
    model: str = Config.DEFAULT_MODEL
    width: int = 512
    height: int = 512
    steps: int = 8

# Option type: a callable that modifies GenerateParameters
GenerateOption = Callable[[GenerateParameters], None]

def with_model(model: str) -> GenerateOption:
    def apply(params: GenerateParameters):
        params.model = model
    return apply

def with_size(width: int, height: int) -> GenerateOption:
    def apply(params: GenerateParameters):
        params.width = width
        params.height = height
    return apply

def with_steps(steps: int) -> GenerateOption:
    def apply(params: GenerateParameters):
        params.steps = steps
    return apply
