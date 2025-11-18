#!/usr/bin/env python3
"""Entry point for the text-to-image generation server."""
from flask import Flask

from config import Config
from controller.healthcheck import healthcheck_blueprint
from model.generator import ImageGenerator
from controller.image import ImageController


def create_app(generator: ImageGenerator) -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)

    image_controller = ImageController(generator)
    app.register_blueprint(image_controller.get_blueprint())
    app.register_blueprint(healthcheck_blueprint)

    return app


def main():
    config = Config().load_from_env()
    
    image_generator = ImageGenerator(config.DEFAULT_MODEL)

    app = create_app(image_generator)
    
    print(f"Starting Text-to-Image Generation Server on port {config.PORT}...")
    print(f"Model: {config.DEFAULT_MODEL}")
    
    app.run(host="0.0.0.0", port=config.PORT)


if __name__ == "__main__":
    main()


