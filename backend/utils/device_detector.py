import torch
from model.device import Device
from enums import DeviceType


class DeviceDetector:
    """Detects on available computation devices with proper inference dtype."""
    
    @staticmethod
    def detect() -> Device:
        """Detect the available computation device."""
        if torch.cuda.is_available():
            print("✅ Detected CUDA (NVIDIA GPU)")
            return Device(type=DeviceType.CUDA, dtype=torch.float16)
        
        elif torch.backends.mps.is_available():
            print("✅ Detected MPS (Apple Silicon)")
            return Device(type=DeviceType.MPS, dtype=torch.float16)
        
        else:
            print("⚠️ No GPU detected, using CPU (inference will be slow)")
            return Device(type=DeviceType.CPU, dtype=torch.float32)
    