class Jsonifiable:
    def to_dict(self) -> dict:
        """
        Convert the object to a JSON-serializable dictionary.
        """
        raise NotImplementedError