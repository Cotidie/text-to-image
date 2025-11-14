from typing import TypeVar, Generic
from view.interface import Parsable

T = TypeVar('T', bound=Parsable)

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

    def parse(self, data: str) -> T:
        """
        Get request data.
        """
        ...
    
    def data(self) -> T:
        """
        Get request data.
        """
        return self._data