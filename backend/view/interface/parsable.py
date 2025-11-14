class Parsable:
    """Interface for parsable request models."""
    
    def from_dict(self, data: dict) -> None:
        """
        Parse the object from a dictionary.
        """
        raise NotImplementedError