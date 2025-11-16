"""Image generation logic"""
from diffusers import StableDiffusionPipeline
from PIL import Image
import torch

from model.generator_option import GenerateParameters, GenerateOption 
from config import Config


class _ImageGenerator:
    """Class for handling image generation with Stable Diffusion model."""
    
    def __init__(self, model: str):
        """Initialize the generator with a specific model."""
        self.model = model
        self._pipe = self._get_pipeline(model)

    def _get_pipeline(self, model: str) -> StableDiffusionPipeline:
        return StableDiffusionPipeline.from_pretrained(
            model,
            torch_dtype=torch.float16,
            variant="fp16"
        ).to("cuda")
    
    def generate(self, prompt: str, *options: GenerateOption) -> Image:
        """
        Generate image from text prompt with optional parameters.
        
        Args:
            prompt: Text description of the image to generate
            *options: Optional parameter modifiers (with_size, with_steps, etc.)
            
        Returns:
            Generated PIL Image
        """
        params = GenerateParameters(prompt=prompt)
        for option in options:
            option(params)
        
        return self._pipe(
            prompt=params.prompt,
            num_inference_steps=params.steps,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]


ImageGenerator = _ImageGenerator(model=Config.DEFAULT_MODEL)