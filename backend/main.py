#!/usr/bin/env python3
import os
from flask import Flask

from config import Config, ConfigBuilder
from model.service.generator import Generator
from model.service.editor import Editor
import model.service.pipeline_option as PipelineOption
from controller import ImageController, HealthController

def create_app(config: Config) -> Flask:
    """Create and configure Flask application."""
    app = Flask(__name__)

    generator = Generator(config.model, config.device)
    generator.prepare(
        PipelineOption.with_cpu_offload(False),
        PipelineOption.with_attention_slicing(True),
        PipelineOption.with_load_to_device(config.device),
    )
    editor = Editor(config.model, config.device)
    editor.prepare_from_pipe(generator.pipe)

    image_controller = ImageController(generator, editor)
    health_controller = HealthController()

    app.register_blueprint(image_controller.get_blueprint(), url_prefix='/api/image')
    app.register_blueprint(health_controller.get_blueprint(), url_prefix='/api/health')

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


