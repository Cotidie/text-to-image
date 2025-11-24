"""Image generation logic"""
from io import BytesIO
from diffusers import AutoPipelineForImage2Image, AutoPipelineForText2Image
from PIL.Image import Image, open
import requests
import torch

from model.generator_option import GenerateParameters, GenerateOption 
from model.device import Device, DeviceType
from model.model import Model, LoadType

class ImageGenerator:
    """Class for handling image generation with Stable Diffusion model."""

    def __init__(self, model: Model, device: Device):
        self.model = model
        self.device = device
        
        self.pipe_text2image = AutoPipelineForText2Image.from_pretrained(
            model.path,
            torch_dtype=self.device.dtype,
        ).to(self.device.type.value)


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
            
        return self.pipe_text2image(
            prompt=params.prompt,
            num_inference_steps=params.steps,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]
    
    def edit(self, prompt: str, image: Image, *options: GenerateOption) -> Image:
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
            
        return self.pipe_image2image(
            prompt=params.prompt,
            image=image,
            num_inference_steps=2,
            guidance_scale=0.0,
            width=image.width,
            height=image.height,
            strength=0.5
        ).images[0]
    
if __name__ == "__main__":
    generator = ImageGenerator(
        model = Model(
            type=LoadType.LOCAL,
            path="/home/cotidie/models/sdxl-turbo"
        ),
        device = Device(
            type=DeviceType.CUDA,
            dtype=torch.float16
        )
    )
    
    response = requests.get('https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/cat.png')
    img = open(BytesIO(response.content)).resize((512, 512))

    generated = generator.edit(
        prompt="cat wizard, gandalf, lord of the rings, detailed, fantasy, cute, adorable, Pixar, Disney, 8k",
        image=img,
    )

    generated.show()
        
        
    
