# Text-to-Image Generation

A simple Flask REST API for generating images from text prompts using Stability AI's SD-Turbo model, **locally**. The server instance is responsible for a single Text2Image model in common scenario where only a single GPU is available.

## Features
- image generation from text prompts
- Docker containerized deployment
- MVC architecture with Flask blueprints
- NVIDIA and AMD GPU support inside Docker

## Environment
- **Host OS**: Ubuntu 24.04
- **GPU**: NVIDIA RTX 4080 SUPER 16GB
- **Python**: 3.11
- **Library**: Flask, HuggingFace
- **Models**: Stable Diffusion (SD-Turbo, SDXL-Turbo)
- **Container**: pytorch with CUDA support

## Project Structure
![mvc-pattern](.images/readme-mvc-pattern.png)  
```
backend/
├─  controller/          # Flask blueprints & route handlers
├─── image/               # API definitions for /image endpoint group
├─── ...
├─ model/               # Business/Domain logic
├─── entity/              # Data classes in domain layer
├─── service/             # Service classes in domain layer
├─ view/                # Request/response models
├─ enums/               
├─ utils/               # system, infra level utility classes
├─ main.py              # Application entry point
└─ config.py            # Configuration & model enums
```

## Prerequisites
- NVIDIA or AMD GPU
  - [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) for NVIDIA GPU
  - [AMD Container Toolkit](https://github.com/ROCm/container-toolkit) for AMD GPU
- Docker

## Quick Start
### Backend


### Frontend


## API Endpoints
### Generate Image
Generates a new image from scratch based on a provided text prompt.

#### Request
```json
{
  "prompt": "str (Required) - The text description of the image to generate.",
  "steps": "int (Optional, default: 8) - Number of inference steps. Higher values may improve quality.",
  "format": "str (Optional, default: 'png') - Output image format (e.g., 'png', 'jpeg')."
}
```

#### Response
```json
{
  "image": "str - Base64 encoded string of the generated image.",
  "time": "float - Time taken to generate the image in seconds.",
  "format": "str - The format of the returned image (e.g., 'PNG')."
}
```

#### Example
```json
curl -X POST http://www.makinteract.com/api/image/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A futuristic city skyline at sunset",
    "steps": 20,
  }' \
  | jq -r '.image' | base64 -d > generated_image.png
```


### Edit Image
Modifies an existing source image based on a text prompt. 

#### Request
```json
{
  "image": "str (Required) - Base64 encoded string of the source image to edit.",
  "prompt": "str (Required) - The text description for the edit.",
  "steps": "int (Optional) - Number of inference steps.",
  "strength": "float (Optional) - Higher values mean more changes(0.0 to 1.0)",
  "format": "str (Optional) - Output image format."
}
```

##### Response
```json
{
  "image": "str - Base64 encoded string of the edited image.",
  "time": "float - Time taken to edit the image in seconds.",
  "format": "str - The format of the returned image."
}
```

#### Example
```json
IMAGE_DATA=$(base64 -w 0 source_image.png)

curl -X POST http://www.makinteract.com/api/image/edit \
  -H "Content-Type: application/json" \
  -d "{
    \"prompt\": \"Make it snowy\",
    \"image\": \"$IMAGE_DATA\",
    \"steps\": 10,
    \"strength\": 0.8
  }" \
  | jq -r '.image' | base64 -d > edited_image.png
```