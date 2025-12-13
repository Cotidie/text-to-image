from flask import Request

def is_form_data(request: Request) -> bool:
    return request.content_type and request.content_type.startswith('multipart/form-data')

def parse_json_data(request: Request) -> dict:
    """
    Extract data from request based on content type.
    Merges form data and files for multipart requests.
    """

    if is_form_data(request):
        data = request.form.to_dict()
        data.update(request.files.to_dict())
        return data
    return request.get_json(force=True) or {}
