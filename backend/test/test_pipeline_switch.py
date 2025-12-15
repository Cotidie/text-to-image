import os
import sys
import torch
backend_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(backend_root)

from model.service.pipeline_option import *

MODEL_PATH = "/etc/model"


def test_pipeline_switch():
    from model.service.editor import Editor
    from model.service.generator import Generator
    from model.entity.model import Model
    from model.service.generator_option import with_steps
    from enums.load_type import LoadType
    from enums.device_type import DeviceType

    # Initialize generator
    generator = Generator(
        Model(type=LoadType.LOCAL, path=MODEL_PATH),
        device=DeviceType.CUDA
    )
    editor = Editor(
        Model(type=LoadType.LOCAL, path=MODEL_PATH),
        device=DeviceType.CUDA
    )
    generator.prepare(
        with_cpu_offload(True),
        with_attention_slicing(True),
        with_load_to_device(DeviceType.CUDA)
    )
    editor.prepare_from_pipe(generator.pipe)

    generated = generator.generate(
        "A cute cat staring at a front door",
        with_steps(10),
    )
    generated.image.convert("RGB").save("generated_image.png")
    edited = editor.edit(
        generated.image,
        "Add a red bow tie to the cat",
        with_steps(10),
    )
    edited.image.convert("RGB").save("edited_image.png")

if __name__ == "__main__":
    test_pipeline_switch()