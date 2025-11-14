"""Flask application for the image generation REST API."""
from flask import Flask

from config import Config
from controller.image import image_blueprint
from controller.healthcheck import healthcheck_blueprint
from model.generator import ImageGenerator


class ImageGenerationServer:
    """Flask application for the image generation REST API."""
    
    def __init__(self, config: Config):
        self.config = config
        self.generator = ImageGenerator(config)
        self.app = Flask(__name__)
        self.app.config['IMAGE_GENERATOR'] = self.generator
        self._register_blueprints()
    
    def _register_blueprints(self) -> None:
        """Register all Flask blueprints."""
        self.app.register_blueprint(image_blueprint)
        self.app.register_blueprint(healthcheck_blueprint)
    
    def run(self, host: str = "0.0.0.0", port: int = 5000, **kwargs) -> None:
        self.app.run(host=host, port=port, **kwargs)


