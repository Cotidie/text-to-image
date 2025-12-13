import os
import sys
import torch
backend_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(backend_root)

from model.pipeline_option import *

MODEL_PATH = "/etc/model"


def test_pipeline_switch():
    from model.editor import Editor
    from model.generator import Generator
    from model.model import Model, LoadType
    from model.device import Device
    from model.generator_option import with_steps

    # Initialize generator
    generator = Generator(
        Model(type=LoadType.LOCAL, path=MODEL_PATH),
        device=Device.CUDA
    )
    editor = Editor(
        Model(type=LoadType.LOCAL, path=MODEL_PATH),
        device=Device.CUDA
    )
    generator.prepare(
        with_cpu_offload(True),
        with_attention_slicing(True),
        with_load_to_device(Device.CUDA)
    )
    editor.prepare_from_pipe(generator.pipe)

    generated_image = generator.generate(
        "A cute cat staring at a front door",
        with_steps(10),
    )
    generated_image.convert("RGB").save("generated_image.png")
    edited_image = editor.edit(
        generated_image,
        "Add a red bow tie to the cat",
        with_steps(10),
    )
    edited_image.convert("RGB").save("edited_image.png")

if __name__ == "__main__":
    test_pipeline_switch()