#!/usr/bin/env python3
"""Entry point for the text-to-image generation server."""
from flask import Flask

from config import Config
from controller.image import image_blueprint
from controller.healthcheck import healthcheck_blueprint


def create_app() -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)

    app.register_blueprint(image_blueprint)
    app.register_blueprint(healthcheck_blueprint)

    return app


def main():
    app = create_app()
    Config.load_from_env()
    
    print(f"Starting Text-to-Image Generation Server on port {Config.PORT}...")
    print(f"Model: {Config.DEFAULT_MODEL}")
    
    app.run(host="0.0.0.0", port=Config.PORT)


if __name__ == "__main__":
    main()


