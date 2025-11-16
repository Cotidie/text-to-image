# Text-to-Image Generation

A simple Flask REST API for generating images from text prompts using Stability AI's SD-Turbo model, **locally**.

## Features
- Fast image generation from text prompts
- GPU-accelerated inference with CUDA support
- Docker containerized deployment
- MVC architecture with Flask blueprints

## Environment
- **OS**: Ubuntu 24.04
- **GPU**: NVIDIA RTX 4080 SUPER 16GB
- **Python**: 3.13
- **Library**: Flask, Diffusers
- **Models**: Stable Diffusion (SD-Turbo, SDXL-Turbo)
- **Container**: Docker with CUDA support

## Project Structure
![mvc-pattern](.images/readme-mvc-pattern.png)  
```
backend/
├── controller/          # Flask blueprints & route handlers
│   ├── image.py             # Image generation endpoints
│   ├── healthcheck.py       # Health check endpoints
│   └── ...
├── model/               # Business logic
│   ├── generator.py         # Image generation with diffusers
│   └── ...
└── view/                # Request/response models
    ├── request/         # Input parsing
    └── response/        # Output formatting
├── main.py              # Application entry point
└── config.py            # Configuration & model enums
```

## Quick Start

### Using Docker (Recommended)
```bash
docker-compose up -d
docker exec -it sd-turbo-server python backend/main.py
```

### Local Setup
```bash
pip install -r requirements.txt
python backend/main.py
```

Server runs on `http://localhost:5000`

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
