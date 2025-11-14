from view.request.image import GenerateImage

class RequestParser:
    """Parser for request models."""
    
    @staticmethod
    def parse_generate_image(data: dict) -> GenerateImage:
        """
        Parse a GenerateImage request from a dictionary.
        """
        generate_image = GenerateImage()
        generate_image.from_dict(data)
        return generate_image