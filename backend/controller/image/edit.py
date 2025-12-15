import io
from flask import request, send_file
from flask.views import MethodView
from model.service.editor import Editor
import model.service.editor_option as Options
from view.request.image.edit import EditImageRequest
from view.response.image.edit import EditImageResponse

class EditImageAPI(MethodView):
    """Handle image editing requests."""
    
    init_every_request = False

    def __init__(self, editor: Editor):
        super().__init__()
        self.editor = editor

    def post(self):
        data = EditImageRequest(request)

        generated = self.editor.edit(
            data.image,
            data.prompt,
            Options.with_steps(data.steps),
            Options.with_strength(data.strength)
        )

        response = EditImageResponse(generated.image, generated.time)
        
        return response.to_dict()

