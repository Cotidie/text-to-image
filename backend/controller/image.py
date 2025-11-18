from flask import Blueprint
from model.generator import ImageGenerator
from controller.image.generate import GenerateImageAPI

class ImageController:
    """Controller for /image endpoint."""
    
    def __init__(self, generator: ImageGenerator):
        self.generateAPI = GenerateImageAPI(generator)
        self.blueprint = Blueprint('image', __name__, url_prefix='/image')

        self.generator = generator
        self._register_routes()

    def get_blueprint(self):
        return self.blueprint

    def _register_routes(self):
        self.blueprint.add_url_rule(
            '/generate',
            view_func=self.generateAPI.as_view(
                '/image/generate', 
                generator=self.generator
            ),
            methods=['POST']
        )