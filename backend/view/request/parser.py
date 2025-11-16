from view.request.image import GenerateImage
from view.request.base import Request
from flask import Request as FlaskRequest

class RequestParser:
    """Parser for request models."""
    
    @staticmethod
    def generate_image(request: FlaskRequest) -> Request[GenerateImage]:
        """
        Parse a GenerateImage request from a flask request.
        """
        generate_image = GenerateImage("")
        generate_image.from_dict(request.get_json(force=True))

        return Request(generate_image)