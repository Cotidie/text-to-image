from dataclasses import dataclass
from typing import Callable

@dataclass    
class GenerateParameters:
    prompt: str
    width: int = 512
    height: int = 512
    steps: int = 8

    def with_image_size(self, width: int, height: int):
        self.width = width
        self.height = height
        return self
    
    def with_steps(self, steps: int):
        self.steps = steps
        return self

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
