from dataclasses import dataclass
from PIL import Image

@dataclass
class GeneratedImage:
    image: Image.Image
    time: float
