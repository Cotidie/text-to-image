import io
from flask import request, send_file
from flask.views import MethodView
from model.image_generator import ImageGenerator
import model.image_generator_option as Options
from view.request.image.generate import GenerateImage

class GenerateImageAPI(MethodView):
    """Handle image generation requests."""

    init_every_request = False

    def __init__(self, generator: ImageGenerator):
        super().__init__()
        self.generator = generator 

    def post(self):
        data = GenerateImage.from_request(request)
        data.validate()

        image = self.generator.generate(
            data.prompt,
            Options.with_steps(data.steps),
            Options.with_size(data.width, data.height),
        )

        image_io = io.BytesIO()
        image.save(image_io, data.format, quality=100)
        image_io.seek(0)
        
        return send_file(
            image_io,
            mimetype=f'image/{data.format}',
            as_attachment=False,
            download_name=f'generated_image.{data.format}'
        )
