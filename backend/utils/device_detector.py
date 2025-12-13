import torch
from model.device import Device


class DeviceDetector:
    """Detects on available computation devices with proper inference dtype."""
    
    @staticmethod
    def detect() -> Device:
        """Detect the available computation device."""
        if torch.cuda.is_available():
            print("✅ Detected CUDA (NVIDIA GPU)")
            return Device.CUDA
        
        elif torch.backends.mps.is_available():
            print("✅ Detected MPS (Apple Silicon)")
            return Device.MPS
        
        else:
            print("⚠️ No GPU detected, using CPU (inference will be slow)")
            return Device.CPU
    