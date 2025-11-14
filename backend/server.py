"""Flask application for the image generation REST API."""
import io

from flask import Flask, request, send_file

from config import Config
from model.generator import ImageGenerator
from view.response.factory import ResponseFactory

class ImageGenerationServer:
    """Flask application for the image generation REST API."""
    
    def __init__(self, config: Config):
        """
        Initialize the Flask server.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.generator = ImageGenerator(config)
        self.app = Flask(__name__)
        self._register_routes()
    
    def _register_routes(self) -> None:
        """Register all Flask routes."""
        self.app.route("/image/generate", methods=["POST", "GET"])(self._generate_image)
        self.app.route("/ping", methods=["GET"])(self._ping)
    
    def _generate_image(self):
        try:
            prompt = self._extract_prompt()

            image = self.generator.generate(prompt=prompt)
            image_io = io.BytesIO()
            image.save(image_io, 'PNG', quality=100)
            image_io.seek(0)

            return send_file(
                image_io, 
                mimetype='image/png', 
                as_attachment=True, 
                download_name='generated_image.png'
            )
        
        except Exception as e:
            print(e)
            return "Error occurred", 500
    
    def _extract_prompt(self) -> str:
        prompt = ""
        if request.method == "POST":
            data = request.get_json(force=True, silent=True) or {}
            prompt = data.get("prompt", "")
        else:
            prompt = request.args.get("prompt", "")

        if prompt == "":
            raise ValueError("Missing 'prompt' parameter")

        return prompt

    def _ping(self):
        return "pong", 200
    
    def run(self, host: str = "0.0.0.0", port: int = 5000, **kwargs) -> None:
        self.app.run(host=host, port=port, **kwargs)
