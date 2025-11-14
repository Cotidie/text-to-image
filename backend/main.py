#!/usr/bin/env python3
"""Entry point for the text-to-image generation server."""
from flask import Flask

from config import Config
from controller.image import image_blueprint
from controller.healthcheck import healthcheck_blueprint
from model.generator import ImageGenerator


def create_app(config: Config) -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)
    app.config['IMAGE_GENERATOR'] = ImageGenerator(config)
    app.register_blueprint(image_blueprint)
    app.register_blueprint(healthcheck_blueprint)
    return app


def main():
    config = Config()
    app = create_app(config)
    
    print(f"Starting Text-to-Image Generation Server on port 5000...")
    print(f"Model: {config.model}")
    
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()


