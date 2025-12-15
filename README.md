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
- **Library**: Flask, HuggingFace, React, Vite
- **Models**: Stable Diffusion (SDXL-Turbo)
- **Container**: pytorch with CUDA support

## Project Structure
![mvc-pattern](.images/readme-mvc-pattern.png)  
```
backend/
├─ controller/          # Flask blueprints & route handlers
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
- Stable Diffusion model files
  - [StabilityAI/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo/tree/main)

## Quick Start
### Backend
1. clone this repository on **the server**
2. Go to `backend` folder
3. Edit .env file
```bash
vi .env

# Model Configuration
LOAD_TYPE = local                            # local or remote
MODEL_NAME = sdxl-turbo                      # (optional) just identifier

# EDIT HERE when LOAD_TYPE is local
MODEL_PATH = /path/to/models/sdxl-turbo # entire model path for local

# EDIT HERE when LOAD_TYPE is remote
MODEL_REPO = StabilityAI/sdxl-3.0-turbo      # repository on Hugging Face

# Server Configuration
PORT=5555
```

4. Run docker compose depending on GPU vendor
```bash
cd backend

docker compose --profile amd up --build -d    # for amd
docker compose --profile nvidia up --build -d # for nvidia
```

5. Now the server runs on '<public IP>:5555'

### Frontend
1. Clone this repository on your **local machine**
2. Go to `frontend` folder
3. Edit .env file to match public ip/domain
```bash
cd frontend
vi .env

VITE_API_TARGET=http://www.makinteract.com   # EDIT here for your public domain
```
4. Run a script for easy deployment
```bash
sudo chmod +x deploy.sh
./deploy.sh
```
5. Now webpage runs on `www.makinteract.com`

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
```bash
curl -X POST http://www.makinteract.com/api/image/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A futuristic city skyline at sunset",
    "steps": 4,
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
⚠️ `curl` in CLI cannot handle such lengthy string for image. Use `.js` script or `.json` file instread.

##### Response
```json
{
  "image": "str - Base64 encoded string of the edited image.",
  "time": "float - Time taken to edit the image in seconds.",
  "format": "str - The format of the returned image."
}
```

#### Example

```bash
# 1. Construct the JSON payload in a temporary file
echo -n '{"prompt": "Make it snowy", "steps": 4, "strength": 0.75, "image": "' > payload.json
base64 -w 0 source_image.png >> payload.json
echo -n '"}' >> payload.json

# 2. Send the request using the file (@payload.json)
curl -X POST http://www.makinteract.com/api/image/edit \
  -H "Content-Type: application/json"
-d @payload.json
| jq -r '.image' | base64 -d > edited_image.png
```