from flask import Request

def parse_data(request: Request) -> dict:
    """
    Extract data from request based on content type.
    Merges form data and files for multipart requests.
    """
    def is_form_data(req: Request) -> bool:
        return req.content_type and req.content_type.startswith('multipart/form-data')

    if is_form_data(request):
        data = request.form.to_dict()
        data.update(request.files.to_dict())
        return data
    return request.get_json(force=True) or {}
