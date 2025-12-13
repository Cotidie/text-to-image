
from dataclasses import dataclass
from typing import Callable
from model.device import Device

@dataclass    
class PipelineParameter:
    cpu_offload: bool = False
    attention_slicing: bool = False
    device: Device = Device.NONE

PipelineOption = Callable[[PipelineParameter], None]

def with_cpu_offload(enabled: bool) -> PipelineOption:
    """Enable or disable CPU offloading for the pipeline"""
    def apply(params: PipelineParameter):
        params.cpu_offload = enabled
    return apply

def with_attention_slicing(enabled: bool) -> PipelineOption:
    """Enable or disable attention slicing for the pipeline"""
    def apply(params: PipelineParameter):
        params.attention_slicing = enabled
    return apply

def with_load_to_device(device: Device) -> PipelineOption:
    """Set the device for loading the pipeline"""
    def apply(params: PipelineParameter):
        params.device = device
    return apply