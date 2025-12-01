


from diffusers import AutoPipelineForImage2Image, DiffusionPipeline
from enums.device_type import DeviceType
from model.image_editor_option import EditParameter, EditOption
from model.pipeline_option import PipelineOption, PipelineParameter
from PIL.Image import Image


class ImageEditor:
    """Class for handling image editing with Stable Diffusion model."""

    def __init__(self):
        self.pipe = None

    def prepare(self, pipe: DiffusionPipeline, *options: PipelineOption):
        """Prepare the editor with a custom pipeline."""
        self.pipe = AutoPipelineForImage2Image.from_pipe(pipe)

        params = PipelineParameter()
        for option in options:
            option(params)
        self._apply_pipeline_options(params)

        print("Pipelines re-initialized with custom pipeline.")

    def edit(self, image: Image, prompt: str, *options: EditOption) -> Image:
        """Edit an image based on the given prompt and options."""
        image = image.convert("RGB")

        params = EditParameter()
        for option in options:
            option(params)

        return self.pipe(
            prompt=prompt,
            image=image,
            strength=params.strength,
            num_inference_steps=params.steps,
            guidance_scale=0.0,
            width=params.width,
            height=params.height
        ).images[0] 
    
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