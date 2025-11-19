#!/usr/bin/env python3
"""Entry point for the text-to-image generation server."""
from flask import Flask

from config import Config
from model.generator import ImageGenerator
from controller import ImageController, HealthController
from utils import DeviceDetector

def create_app(config: Config) -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)

    image_generator = ImageGenerator(config.model, config.device)
    image_controller = ImageController(image_generator)
    health_controller = HealthController()

    app.register_blueprint(image_controller.get_blueprint())
    app.register_blueprint(health_controller.get_blueprint())

    return app


def main():
    config = Config().load_from_env()
    config.device = DeviceDetector.detect()
    
    app = create_app(config)
    
    print(f"Starting Text-to-Image Generation Server on port {config.port}...")
    print(f"Model: {config.model}")
    
    app.run(host="0.0.0.0", port=config.port)


if __name__ == "__main__":
    main()


