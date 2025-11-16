from abc import ABC, abstractmethod

class Parsable(ABC):
    """Interface for parsable request models."""
    
    @abstractmethod
    def from_dict(self, data: dict) -> None:
        """
        Parse the object from a dictionary.
        """
        raise NotImplementedError