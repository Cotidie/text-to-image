#!/usr/bin/env python3
"""Entry point for the text-to-image generation server."""
from flask import Flask

from config import Config
from controller.image import image_bp
from controller.healthcheck import healthcheck_bp
from model.generator import ImageGenerator


def create_app(config: Config) -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)
    app.config['IMAGE_GENERATOR'] = ImageGenerator(config)
    app.register_blueprint(image_bp)
    app.register_blueprint(healthcheck_bp)
    return app


def main():
    config = Config()
    app = create_app(config)
    
    print(f"Starting Text-to-Image Generation Server on port 5000...")
    print(f"Model: {config.model}")
    
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()


