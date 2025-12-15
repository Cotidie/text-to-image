from dataclasses import dataclass
from PIL.Image import Image
from view.interface import Serializable
import base64

@dataclass
class EditImageResponse(Serializable):
    """
    Data payload for image editing endpoint
    
    Attributes:
        image (Image): The edited image.
        time (float): The time taken to edit the image.
        format (str): The format of the image.
    """
    image: Image
    time: float
    format: str = "PNG"
    
    def to_dict(self) -> dict:
        return {
            "image": base64.b64encode(self.image.tobytes()).decode('utf-8'),
            "format": self.format,
            "time": self.time,
        }