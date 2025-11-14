
"""Image generation logic"""
from diffusers import AutoPipelineForText2Image, StableDiffusionPipeline
from PIL import Image

import torch

from config import Config


_pipe: StableDiffusionPipeline = None

def _setup_pipeline(self):
    pipe = AutoPipelineForText2Image.from_pretrained(
        self.config.model, 
        torch_dtype=torch.float16, 
        variant="fp16"
    )
    pipe.to("cuda")

    return pipe

class ImageGenerator:
    """Handles image generation requests to Stable Diffusion model."""
    
    def __init__(self, config: Config = Config()):
        global _pipe
        if _pipe is None:
            _pipe = _setup_pipeline()

        self.config: Config = config
        self.pipe = _pipe
    
    def generate(self, prompt: str) -> Image:
        return self.pipe(
            prompt=prompt, 
            num_inference_steps=8, 
            guidance_scale=0.0
        ).images[0]


if __name__ == "__main__":
    generator = ImageGenerator()
    result = generator.generate("hello world")
    result.show()