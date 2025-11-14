from typing import TypeVar, Generic, Union
from view.interface import Parsable, Validatable

T = TypeVar('T', bound=Union[Parsable, Validatable])

class Request(Generic[T]):
    """
    Generic request interface that all request types must implement.
    """

    def __init__(self, data: T=None, method: str=""):
        self._data: T = data
        self._method: str= method

    def method(self) -> str:
        """
        Get HTTP method for this request.
        """
        return self._method
    
    def data(self) -> T:
        """
        Get request data.
        """
        return self._data
    
    def parse(self, data: str) -> T:
        """
        Get request data.
        """
        ...

    def validate(self) -> None:
        """
        Validate request data.
        """
        if self._data:
            self._data.validate()