#!/usr/bin/env python3
"""Entry point for the text-to-image generation server."""
from flask import Flask

from config import Config
from controller.image import image_blueprint
from controller.healthcheck import healthcheck_blueprint
from model.generator import ImageGenerator


def create_app() -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)
    app.register_blueprint(image_blueprint)
    app.register_blueprint(healthcheck_blueprint)

    return app


def main():
    config = Config().load_from_env()
    ImageGenerator.initialize(config.DEFAULT_MODEL)

    app = create_app()
    
    print(f"Starting Text-to-Image Generation Server on port {config.PORT}...")
    print(f"Model: {config.DEFAULT_MODEL}")
    
    app.run(host="0.0.0.0", port=config.PORT)


if __name__ == "__main__":
    main()


