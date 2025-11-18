from flask import Blueprint
from model.generator import ImageGenerator

from .generate import GenerateImageAPI

class ImageController:
    """Controller for /image endpoint."""

    PREFIX = "/image"
    
    def __init__(self, generator: ImageGenerator):
        self.blueprint = Blueprint('image', __name__, url_prefix=self.PREFIX)
        self.generator = generator

        self._register_routes()

    def get_blueprint(self):
        return self.blueprint

    def _register_routes(self):
        self.blueprint.add_url_rule(
            '/generate',
            view_func=GenerateImageAPI.as_view(
                '/image/generate',
                generator=self.generator
            ),
            methods=['POST']
        )