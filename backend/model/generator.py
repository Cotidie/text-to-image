
"""Image generation logic"""
from diffusers import AutoPipelineForText2Image, StableDiffusionPipeline
from PIL import Image

import torch

from model.generate_options import GenerateParameters, GenerateOption

_pipe: StableDiffusionPipeline = None

def _setup_pipeline(model: str):
    pipe = AutoPipelineForText2Image.from_pretrained(
        model, 
        torch_dtype=torch.float16, 
        variant="fp16"
    )
    pipe.to("cuda")

    return pipe

class ImageGenerator:
    """Handles image generation requests to Stable Diffusion model."""
    
    def __init__(self):
        global _pipe
        if _pipe is None:
            _pipe = _setup_pipeline()

        self.pipe = _pipe
    
    def generate(self, prompt: str, *options: GenerateOption) -> Image:
        params = GenerateParameters(prompt=prompt)
        for option in options:
            option(params)
        
        return self.pipe(
            prompt=params.prompt, 
            num_inference_steps=params.steps, 
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]


if __name__ == "__main__":
    generator = ImageGenerator()
    result = generator.generate("hello world")
    result.show()