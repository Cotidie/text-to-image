from dataclasses import dataclass
from enums import DeviceType
import torch

@dataclass
class Device:
    """Represents a computation device with its type(CUDA, MPS, CPU, ...) and data type. Use DeviceDetector in utils module to instantiate."""
    
    type: DeviceType
    dtype: torch.dtype
        

