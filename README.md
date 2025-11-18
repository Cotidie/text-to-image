# Text-to-Image Generation

A simple Flask REST API for generating images from text prompts using Stability AI's SD-Turbo model, **locally**. The server instance is responsible for a single Text2Image model in common scenario where only a single GPU is available.

## Features
- Fast image generation from text prompts
- GPU-accelerated inference with CUDA support
- Docker containerized deployment
- MVC architecture with Flask blueprints

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
├─ controller/          # Flask blueprints & route handlers
├─ model/               # Business/Domain logic
├─ view/                # Request/response models
├── main.py              # Application entry point
└── config.py            # Configuration & model enums
```

## Quick Start
1. Install NVIDIA container toolkit

| https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

2. Download a model package (folder) containing .safetensors 
  - Put the model folder into `models/`

| ex) https://huggingface.co/stabilityai/sd-turbo/tree/main

3. Build a docker
```bash
docker build -t text-to-image:local .
```

4. Configure environment variables
  - edit `.env` to choose a model to run
    - `DEFAULT_MODEL=/app/models/sd-turbo`

5. Run docker-compose
```bash
docker compose up -d
```

6. Now your server runs on the port on `.env`

## API Endpoints

### Generate Image
**POST** `/image/generate`

Request body:
```json
{
  "prompt": "a cat on a skateboard",
  "width": 512,
  "height": 512,
  "steps": 8
}
```

Parameters:
- `prompt` (required): Text description of the image
- `width` (optional): Image width in pixels (default: 512)
- `height` (optional): Image height in pixels (default: 512)
- `steps` (optional): Number of inference steps (default: 8)

Example:
```bash
curl -X POST http://localhost:5000/image/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "a sunset over mountains", "width": 768, "height": 512, "steps": 10}' \
  --output image.png
```

### Health Check
**GET** `/ping`

```bash
curl http://localhost:5000/ping
# Returns: "pong"
```

## License
Educational purposes.
