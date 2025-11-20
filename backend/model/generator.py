"""Image generation logic"""
from diffusers import AutoPipelineForText2Image, DiffusionPipeline
from PIL import Image

from model.generator_option import GenerateParameters, GenerateOption 
from model.device import Device
from model.model import Model

class ImageGenerator:
    """Class for handling image generation with Stable Diffusion model."""

    def __init__(self, model: Model, device: Device):
        self.model = model
        self.device = device
        self._pipe = self._get_pipeline(model.path)
    
    def generate(self, prompt: str, *options: GenerateOption) -> Image:
        """
        Generate image from text prompt with optional parameters.
        
        Args:
            prompt: Text description of the image to generate
            *options: Optional parameter modifiers (with_size, with_steps, etc.)
            
        Returns:
            Generated PIL Image
        """
        print(f"Generating image for prompt: {prompt}")

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
    
    def generate(self, prompt: str, image: Image, *options: GenerateOption) -> Image:
        """
        Generate image from text prompt and input image with optional parameters.
        
        Args:
            prompt: Text description of the image to generate
            image: Input PIL Image for image-to-image generation
            *options: Optional parameter modifiers (with_size, with_steps, etc.)
            
        Returns:
            Generated PIL Image
        """
        print(f"Generating image for prompt: {prompt} with input image.")

        params = GenerateParameters(prompt=prompt)
        for option in options:
            option(params)
            
        return self._pipe(
            prompt=params.prompt,
            init_image=image,
            num_inference_steps=params.steps,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]
    
    def _get_pipeline(self, model_path: str) -> DiffusionPipeline:
        return AutoPipelineForText2Image.from_pretrained(
            model_path,
            torch_dtype=self.device.dtype,
        ).to(self.device.type.value)