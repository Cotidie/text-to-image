import io
from flask import request, send_file
from flask.views import MethodView
from model.service.editor import Editor
import model.service.editor_option as Options
from view.request.image.edit import EditImage

class EditImageAPI(MethodView):
    """Handle image editing requests."""
    
    init_every_request = False

    def __init__(self, editor: Editor):
        super().__init__()
        self.editor = editor

    def post(self):
        data = EditImage(request)
        data.validate()

        generated_image = self.editor.edit(
            data.image,
            data.prompt,
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
