from dataclasses import dataclass
from PIL import Image

@dataclass
class EditedImage:
    image: Image.Image
    time: float
