from dataclasses import dataclass
from enums import DeviceType
import torch

@dataclass
class Device:
    """Represents a computation device with its type(CUDA, MPS, CPU, ...) and data type. Use DeviceDetector in utils module to instantiate."""
    
    type: DeviceType
    dtype: torch.dtype


class PredefinedDevices:
    """Predefined device configurations."""
    
    CUDA = Device(type=DeviceType.CUDA, dtype=torch.float16)
    MPS = Device(type=DeviceType.MPS, dtype=torch.float16)
    CPU = Device(type=DeviceType.CPU, dtype=torch.float32)
        

