#!/usr/bin/env python3
"""Entry point for the text-to-image generation server."""
from flask import Flask

from config import *
from controller.image import image_blueprint
from controller.healthcheck import healthcheck_blueprint


def create_app(config: Config) -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)

    app.config[MODEL] = config.model
    app.config[DEFAULT_WIDTH] = config.default_width
    app.config[DEFAULT_HEIGHT] = config.default_height
    app.config[DEFAULT_STEPS] = config.default_steps
    app.config[TIMEOUT] = config.timeout

    app.register_blueprint(image_blueprint)
    app.register_blueprint(healthcheck_blueprint)
    return app


def main():
    config = Config()
    app = create_app(config)
    
    print(f"Starting Text-to-Image Generation Server on port 5006...")
    print(f"Model: {config.model}")
    
    app.run(host="0.0.0.0", port=5006)


if __name__ == "__main__":
    main()


