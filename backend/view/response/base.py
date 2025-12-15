from typing import TypeVar, Generic
from flask import jsonify

from view.interface import Serializable

T = TypeVar('T', bound=Serializable)

class Response(Generic[T]):
    """
    Generic response interface that all response types must implement.
    """

    def __init__(self, data: T=None, status_code: int=200):
        self._data = data
        self._status_code = status_code

    def json(self) -> str:
        """
        Convert response to JSON string.
        """
        return jsonify({
            "data": self.data().to_dict(),
            "status": self.status()
        })
    
    def status(self) -> int:
        """
        Get HTTP status code for this response.
        """
        return self._status_code

    def data(self) -> T:
        """
        Get response data.
        """
        return self._data