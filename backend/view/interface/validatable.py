class Validatable:
    """
    Interface for validatable objects.
    """
    def validate(self) -> None:
        """
        Validate the object's data.

        Raises:
            ValueError: If validation fails.
        """
        ...