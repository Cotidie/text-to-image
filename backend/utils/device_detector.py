import torch
from enums.device_type import DeviceType


class DeviceDetector:
    """Detects on available computation devices with proper inference dtype."""
    
    @staticmethod
    def detect() -> DeviceType:
        """Detect the available computation device."""
        if torch.cuda.is_available():
            print("✅ Detected CUDA (NVIDIA GPU)")
            return DeviceType.CUDA
        
        elif torch.backends.mps.is_available():
            print("✅ Detected MPS (Apple Silicon)")
            return DeviceType.MPS
        
        else:
            print("⚠️ No GPU detected, using CPU (inference will be slow)")
            return DeviceType.CPU
    