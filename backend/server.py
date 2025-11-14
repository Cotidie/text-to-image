"""Flask application for the image generation REST API."""
from flask import Flask

from config import Config
from controller import image, healthcheck
from model.generator import ImageGenerator


class ImageGenerationServer:
    """Flask application for the image generation REST API."""
    
    def __init__(self, config: Config):
        self.config = config
        self.generator = ImageGenerator(config)
        self.app = Flask(__name__)
        self._register_routes()
    
    def _register_routes(self) -> None:
        """Register all Flask routes."""
        self.app.route("/image/generate", methods=["POST", "GET"])(
            lambda: image.generate_image(self.generator)
        )
        self.app.route("/ping", methods=["GET"])(healthcheck.ping)
    
    def run(self, host: str = "0.0.0.0", port: int = 5000, **kwargs) -> None:
        self.app.run(host=host, port=port, **kwargs)

