"""Image generation logic"""
from diffusers import AutoPipelineForText2Image
from PIL.Image import Image
from model.generator_option import GenerateParameters, GenerateOption 
from model.device import Device
from model.model import Model

class ImageGenerator:
    """Class for handling image generation with Stable Diffusion model."""

    def __init__(self, model: Model, device: Device):
        self.model = model
        self.device = device
        
        self.pipe = AutoPipelineForText2Image.from_pretrained(
            model.path,
            torch_dtype=self.device.dtype,
            use_safetensors=True,
        ).to(self.device.type.value)

        self.pipe.enable_vae_tiling()
        self.pipe.enable_vae_slicing()
        print("Pipelines initialized.")


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
            
        return self.pipe(
            prompt=params.prompt,
            num_inference_steps=params.steps,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]
        