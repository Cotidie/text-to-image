from enum import Enum

class DeviceType(str, Enum):
    """Supported device types."""
    CUDA = "cuda"  # NVIDIA GPUs
    AMD = "cuda"   # AMD uses ROCm which is compatible with CUDA
    MPS = "mps"    # Apple Silicon
    CPU = "cpu"
    
