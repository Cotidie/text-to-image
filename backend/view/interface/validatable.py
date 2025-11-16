from abc import ABC, abstractmethod

class Validatable(ABC):
    """
    Interface for validatable objects.
    """
    
    @abstractmethod
    def validate(self) -> None:
        """
        Validate the object's data.

        Raises:
            ValueError: If validation fails.
        """
        raise NotImplementedError