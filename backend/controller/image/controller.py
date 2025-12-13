from flask import Blueprint
from model.editor import Editor
from model.generator import Generator

from .generate import GenerateImageAPI
from .edit import EditImageAPI

class ImageController:
    """Controller for /image endpoint."""

    PREFIX = "/image"
    
    def __init__(self, generator: Generator, editor: Editor):
        self.blueprint = Blueprint('image', __name__, url_prefix=self.PREFIX)
        self.generator = generator
        self.editor = editor
    
        self._register_routes()

    def get_blueprint(self):
        return self.blueprint

    def _register_routes(self):
        self.blueprint.add_url_rule(
            '/generate',
            view_func=GenerateImageAPI.as_view(
                'generate-image',
                generator=self.generator
            ),
            methods=['POST']
        )
        self.blueprint.add_url_rule(
            '/edit',
            view_func=EditImageAPI.as_view(
                'edit-image',
                editor=self.editor
            ),
            methods=['POST']
        )