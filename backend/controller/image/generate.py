import io
from flask import request, send_file
from flask.views import MethodView
from model.service.generator import Generator
import model.service.generator_option as Options
from view.request.image.generate import GenerateImageRequest
from view.response.image.generate import GenerateImageResponse

class GenerateImageAPI(MethodView):
    """Handle image generation requests."""

    init_every_request = False

    def __init__(self, generator: Generator):
        super().__init__()
        self.generator = generator 

    def post(self):
        data = GenerateImageRequest(request)

        generated = self.generator.generate(
            data.prompt,
            Options.with_steps(data.steps),
            Options.with_size(data.width, data.height),
        )

        response = GenerateImageResponse(generated.image, generated.time)
        
        return response.to_dict()
