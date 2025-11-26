#!/usr/bin/env python3
from flask import Flask

from config import Config, ConfigBuilder
from model.generator import ImageGenerator
from controller import ImageController, HealthController

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
    config = ConfigBuilder()\
        .with_port(5555)\
        .with_env()\
        .build()

    app = create_app(config)
    
    print(f"Starting Text-to-Image Generation Server on port {config.port}...")
    print(f"Model: {config.model}")

    try:
        app.run(host="0.0.0.0", port=config.port)
    except Exception as e:
        print(f"Error running the server: {e}")


if __name__ == "__main__":
    main()


