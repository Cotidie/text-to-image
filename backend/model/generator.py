"""Image generation logic"""
from diffusers import StableDiffusionPipeline
from PIL import Image
import torch

from model.generator_option import GenerateParameters, GenerateOption 

class ImageGenerator:
    """Class for handling image generation with Stable Diffusion model."""

    _instance = None

    def __init__(self, model: str):
        """Initialize the generator with a specific model."""
        if ImageGenerator._instance == None:
            self.model = model
            self._pipe = self._get_pipeline(model)
            ImageGenerator._instance = self

    @classmethod
    def initialize(cls, model: str):
        cls._instance = ImageGenerator(model)

    def _get_pipeline(self, model: str) -> StableDiffusionPipeline:
        return StableDiffusionPipeline.from_pretrained(
            model,
            torch_dtype=torch.float16,
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
        
        return ImageGenerator._instance._pipe(
            prompt=params.prompt,
            num_inference_steps=params.steps,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]
