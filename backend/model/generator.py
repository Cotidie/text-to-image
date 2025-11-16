"""Image generation logic"""
from diffusers import AutoPipelineForText2Image, StableDiffusionPipeline
from PIL import Image
import torch

from model.generator_option import GenerateParameters, GenerateOption


class ImageGenerator:
    """Singleton class for handling image generation with Stable Diffusion model."""
    
    _pipes: dict[str, StableDiffusionPipeline] = {}

    @classmethod
    def _get_pipeline(cls, model: str) -> StableDiffusionPipeline:
        if model not in cls._pipes:
            cls._pipes[model] = AutoPipelineForText2Image.from_pretrained(
                model,
                torch_dtype=torch.float16,
                variant="fp16"
            )
            cls._pipes[model].to("cuda")
        
        return cls._pipes[model]
    
    @staticmethod
    def generate(prompt: str, *options: GenerateOption) -> Image:
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
        
        pipe = ImageGenerator._get_pipeline(params.model)
        
        return pipe(
            prompt=params.prompt,
            num_inference_steps=params.steps,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]
