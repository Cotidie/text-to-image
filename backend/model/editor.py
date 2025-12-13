from diffusers import AutoPipelineForImage2Image
from PIL.Image import Image
from model.editor_option import EditOption, EditParameter
from model.pipeline_option import PipelineParameter, PipelineOption
from model.model import Model
from enums.device_type import DeviceType

class Editor:
    """Class for handling image editor with Stable Diffusion model."""

    def __init__(self, model: Model, device: DeviceType):
        self.model = model
        self.device = device
        self.pipe = None

    def prepare(self, *options: PipelineOption):
        """Prepare the generator with a new model and device."""
        dtype = torch.float16
        if self.device == DeviceType.CPU:
            dtype = torch.float32

        self.pipe = AutoPipelineForImage2Image.from_pretrained(
            self.model.path,
            torch_dtype=dtype,
            use_safetensors=True,
        )

        params = PipelineParameter()
        for option in options:
            option(params)
        self._apply_pipeline_options(params)

        print("Pipelines re-initialized with new model and device.")

    def prepare_from_pipe(self, pipe, *options: PipelineOption):
        """Prepare the generator with a custom pipeline."""
        self.pipe = AutoPipelineForImage2Image.from_pipe(pipe)
        
        params = PipelineParameter()
        for option in options:
            option(params)
        self._apply_pipeline_options(params)

    def edit(self, image: Image, prompt: str, *options: EditOption) -> Image:
        """
        Generate image from text prompt with optional parameters.
        
        Args:
            image: Input PIL Image to be edited
            prompt: Text description of the image to generate
            *options: Optional parameter modifiers (with_size, with_steps, etc.)
            
        Returns:
            Generated PIL Image
        """
        print(f"Generating image for prompt: {prompt}")

        image = image.convert("RGB")
        params = EditParameter(prompt=prompt)
        for option in options:
            option(params)

        if params.steps * params.strength < 1:
            raise ValueError("The product of steps and strength must be at least 1.")
            
        return self.pipe(
            image = image,
            prompt=params.prompt,
            num_inference_steps=params.steps,
            strength=params.strength,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0]
    
    def unload_to_cpu(self):
        if self.pipe is not None:
            self.pipe = self.pipe.to("cpu")

    def load_to_device(self):
        if self.pipe is not None:
            self.pipe = self.pipe.to(self.device.value)
    
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
        