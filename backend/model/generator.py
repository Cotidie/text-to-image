"""Image generation logic"""
from diffusers import StableDiffusionPipeline
from PIL import Image
import torch

from model.generator_option import GenerateParameters, GenerateOption 
from enums import DeviceType

class ImageGenerator:
    """Class for handling image generation with Stable Diffusion model."""

    def __init__(self, model: str):
        self.model = model
        self._pipe = self._get_pipeline(model)

    def _get_pipeline(self, model: str) -> StableDiffusionPipeline:
        device, dtype = self._detect_device()

        return StableDiffusionPipeline.from_pretrained(
            model,
            torch_dtype=dtype,
        ).to(device.value)
    
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

    # TODO: can be further devided to DeviceManager class to return Device
    def _detect_device(self):
        """Detect the available device type."""

        if torch.cuda.is_available():
            print("✅ Using CUDA (NVIDIA GPU)")
            return DeviceType.CUDA, torch.float16
        elif torch.backends.mps.is_available():
            print("✅ Using MPS (Apple Silicon)")
            return DeviceType.MPS, torch.float16
        else:
            print("⚠️ Using CPU (Fallback)")
            return DeviceType.CPU, torch.float32