"""Image generation controller."""
import io

from flask import send_file

from model.generator import ImageGenerator
from backend.view.request.image import GenerateImageRequest


def generate_image(generator: ImageGenerator):
    """
    Handle image generation requests.
    
    Args:
        generator: ImageGenerator instance
        
    Returns:
        Flask response with generated image or error
    """
    try:
        req = GenerateImageRequest.from_flask_request()
        
        image = generator.generate(prompt=req.prompt)
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
