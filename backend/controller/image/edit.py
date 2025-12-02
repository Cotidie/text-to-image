import io
from flask import request, send_file
from flask.views import MethodView
from model.generator import ImageGenerator
import model.generator_option as Options
from view.request.image.edit import EditImage

class EditImageAPI(MethodView):
    """Handle image editing requests."""
    
    init_every_request = False

    def __init__(self, generator: ImageGenerator):
        super().__init__()
        self.generator = generator

    def post(self):
        data = EditImage.from_request(request)
        data.validate()

        generated_image = self.generator.edit(
            data.prompt,
            data.image,
            Options.with_steps(data.steps),
            Options.with_strength(data.strength)
        )

        image_io = io.BytesIO()
        generated_image.save(image_io, 'PNG', quality=95)
        image_io.seek(0)
        
        return send_file(
            image_io,
            mimetype='image/png',
            as_attachment=False,
            download_name='edited_image.png'
        )
