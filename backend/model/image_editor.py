


from diffusers import AutoPipelineForImage2Image, DiffusionPipeline
from enums.device_type import DeviceType
from model.image_generator_option import GenerateOption, GenerateParameter
from model.pipeline_option import PipelineOption, PipelineParameter
from PIL.Image import Image


class ImageEditor:
    """Class for handling image editing with Stable Diffusion model."""

    def __init__(self):
        self.pipe = None

    def prepare(self, pipe: DiffusionPipeline, *options: PipelineOption):
        """Prepare the editor with a custom pipeline."""
        self.pipe = AutoPipelineForImage2Image.from_pipe(pipe)
        self.pipe.enable_vae_tiling()
        self.pipe.enable_vae_slicing()
        
        params = PipelineParameter()
        for option in options:
            option(params)
        self._apply_pipeline_options(params)

        print("Pipelines re-initialized with custom pipeline.")

    def edit(self, image: Image, prompt: str, *options: GenerateOption) -> Image:
        """Edit an image based on the given prompt and options."""
        image = image.convert("RGB")

        params = GenerateParameter()
        for option in options:
            option(params)

        return self.pipe(
            prompt=prompt,
            init_image=image,
            strength=params.strength,
            num_inference_steps=params.num_inference_steps,
            guidance_scale=params.guidance_scale,
            width=params.width,
            height=params.height
        ).images[0] 
    
    def _apply_pipeline_options(self, params: PipelineParameter):
        if params.enable_attention_slicing:
            self.pipe.enable_attention_slicing()
        if params.enable_sequential_cpu_offload:
            self.pipe.enable_sequential_cpu_offload()
        if params.device != DeviceType.NONE:
            self.pipe.to(params.device.value)