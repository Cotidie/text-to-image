import io

from flask import Blueprint, request, send_file
from model.generator import ImageGenerator
from view.request.parser import RequestParser
from config import Config

image_blueprint = Blueprint('image', __name__, url_prefix='/image')

@image_blueprint.route("/generate", methods=["POST"])
def generate_image():
    """Handle image generation requests."""
    try:
        req = RequestParser.generate_image(request)
        req.validate()

        data = req.data()
        image = ImageGenerator(
            model=Config.model
        ).generate(prompt=data.prompt)

        image_io = io.BytesIO()
        image.save(image_io, data.format, quality=100)
        image_io.seek(0)
        
        return send_file(
            image_io,
            mimetype=f'image/{data.format}',
            as_attachment=True,
            download_name=f'generated_image.{data.format}'
        )
    
    except Exception as e:
        print(f"Error generating image: {e}")
        return str(e), 500

