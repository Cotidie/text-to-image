from view.response.payload import *
from view.response.base import Response

class ResponseFactory:
    @staticmethod
    def generateImage(
        image: Image.Image, 
        format: str = "PNG", 
        status_code: int = 200
    ) -> Response[GenerateImage]:
        return Response[GenerateImage](
            data=GenerateImage(image=image, format=format),
            status_code=status_code
        )