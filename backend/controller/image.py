import io

from flask import Blueprint, request, send_file, current_app as app
from endpoint import GENERATE_IMAGE
from model.generator import ImageGenerator
from view.request.parser import RequestParser
from config import ConfigKey

image_blueprint = Blueprint('image', __name__, url_prefix='/image')


@image_blueprint.route(GENERATE_IMAGE.path, methods=GENERATE_IMAGE.methods)
def generate_image():
    """
    Handle image generation requests.
    
    Returns:
        Flask response with generated image or error
    """
    try:
        req = RequestParser.parse_generate_image(request)
        req.validate()

        data = req.data()
        image = ImageGenerator(
            model=app.config[ConfigKey.MODEL]
        ).generate(prompt=data.prompt)

        image_io = io.BytesIO()
        image.save(image_io, 'PNG', quality=100)
        image_io.seek(0)
        
        return send_file(
            image_io,
            mimetype='image/png',
            as_attachment=True,
            download_name='generated_image.png'
        )
    
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        print(f"Error generating image: {e}")
        return "Error occurred", 500

