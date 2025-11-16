"""Image generation logic"""
from diffusers import AutoPipelineForText2Image, StableDiffusionPipeline
from PIL import Image
import torch

from model.generator_option import GenerateParameters, GenerateOption 

class ImageGenerator:
    """Singleton class for handling image generation with Stable Diffusion model."""
    
    _pipe: StableDiffusionPipeline = None

    @classmethod
    def _get_pipeline(cls, model: str) -> StableDiffusionPipeline:
        if cls._pipe is None:
            cls._pipe = AutoPipelineForText2Image.from_pretrained(
                model,
                torch_dtype=torch.float16,
                variant="fp16"
            ).to("cuda")
        
        return cls._pipe
    
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

if __name__ == "__main__":
    # Simple test
    img = ImageGenerator.generate(
        "A fantasy landscape, trending on artstation",
    )
    ImageGenerator._pipe.save_pretrained("./model/sdxl-turbo")