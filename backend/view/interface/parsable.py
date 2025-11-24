from abc import ABC, abstractmethod
from typing import TypeVar, Type
from flask import Request

T = TypeVar('T', bound='Parsable')

class Parsable(ABC):
    """Interface for parsable request models."""
    
    @classmethod
    @abstractmethod
    def from_request(cls: Type[T], request: Request) -> T:
        """
        Parse the object from a Flask request.
        """
        raise NotImplementedError