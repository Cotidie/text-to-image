from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        """
        Convert the object to a JSON-serializable dictionary.
        """
        raise NotImplementedError