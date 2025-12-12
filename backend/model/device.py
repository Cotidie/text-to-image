from dataclasses import dataclass
from enum import Enum
import torch

class DeviceType(str, Enum):
    """Supported device types."""
    CUDA = "cuda"  # NVIDIA GPUs
    AMD = "cuda"   # AMD uses ROCm which is compatible with CUDA
    MPS = "mps"    # Apple Silicon
    CPU = "cpu"
    NONE = "none" 
    

@dataclass
class Device:
    """Represents a computation device with its type(CUDA, MPS, CPU, ...) and data type. Use DeviceDetector in utils module to instantiate."""
    
    type: DeviceType
    dtype: torch.dtype

