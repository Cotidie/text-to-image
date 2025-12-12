from diffusers import AutoPipelineForText2Image
from PIL.Image import Image
from model.generator_option import GenerateParameter, GenerateOption 
from model.pipeline_option import PipelineParameter, PipelineOption
from model.device import Device
from model.model import Model
from enums.device_type import DeviceType

class TextToImageGenerator:
    """Class for handling image generation with Stable Diffusion model."""

    def __init__(self, model: Model, device: Device):
        self.model = model
        self.device = device
        self.pipe = None

    def prepare(self, *options: PipelineOption):
        """Prepare the generator with a new model and device."""
        self.pipe = AutoPipelineForText2Image.from_pretrained(
            self.model.path,
            torch_dtype=self.device.dtype,
            use_safetensors=True,
        )

        params = PipelineParameter()
        for option in options:
            option(params)
        self._apply_pipeline_options(params)

        print("Pipelines re-initialized with new model and device.")

    def prepare_from_pipe(self, pipe, *options: PipelineOption):
        """Prepare the generator with a custom pipeline."""
        self.pipe = AutoPipelineForText2Image.from_pipe(pipe)
        
        params = PipelineParameter()
        for option in options:
            option(params)
        self._apply_pipeline_options(params)

        print("Pipelines re-initialized with custom pipeline.")

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

        params = GenerateParameter(prompt=prompt)
        for option in options:
            option(params)
            
        return self.pipe(
            prompt=params.prompt,
            num_inference_steps=params.steps,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]
    
    def unload_to_cpu(self):
        if self.pipe is not None:
            self.pipe = self.pipe.to("cpu")

    def load_to_device(self, device: DeviceType):
        if self.pipe is not None:
            self.pipe = self.pipe.to(device.value)
    
    def _apply_pipeline_options(self, params: PipelineParameter):
        if params.attention_slicing:
            print("✅ attention slicing enabled")
            self.pipe.enable_attention_slicing()
        if params.cpu_offload:
            print("✅ CPU offload enabled") 
            self.pipe.enable_model_cpu_offload()
        if params.device != DeviceType.NONE:
            print("✅ loading pipeline to device:", params.device.value)
            self.pipe = self.pipe.to(params.device.value)
        