#!/usr/bin/env python3
import os
from flask import Flask

from config import Config, ConfigBuilder
from model.generator import ImageGenerator
import model.pipeline_option as PipelineOption
from controller import ImageController, HealthController

def create_app(config: Config) -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)

    generator = ImageGenerator(config.model, config.device)
    generator.prepare(
        PipelineOption.with_cpu_offload(False),
        PipelineOption.with_attention_slicing(True),
        PipelineOption.with_load_to_device(config.device.type),
    )

    image_controller = ImageController(generator)
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
    print(f"Device: {os.getenv('MODEL_PATH', 'NOWAYYY')}")

    try:
        app.run(host="0.0.0.0", port=config.port)
    except Exception as e:
        print(f"Error running the server: {e}")

if __name__ == "__main__":
    main()


