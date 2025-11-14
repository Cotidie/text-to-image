# Text-to-Image Generation

A local Flask REST API for generating images from text prompts using Stability AI's SD-Turbo model, **locally**.

## Features
- Fast image generation from text prompts
- GPU-accelerated inference with CUDA support
- Docker containerized deployment
- MVC architecture for clean and scalable backend structure

## Structure
![mvc-pattern](.images/readme-mvc-pattern.png)  
```
backend/
├── controller/    # Route definitions
├── model/         # Image generation logic
└── view/          # Request/response models
```


## Tech Stack
- **Model**: Stable Diffusion Turbo (stabilityai/sd-turbo)
- **Backend**: Flask, Python 3.10+
- **ML Libraries**: Diffusers, Transformers, Accelerate
- **Container**: Docker with NVIDIA GPU support

## Quick Start

### Using Docker (Recommended)
```bash
docker-compose up -d
docker exec -it sd-turbo-server python main.py
```

### Local Setup
```bash
pip install -r requirements.txt
python main.py
```

Server runs on `http://localhost:5000`

## API Endpoints

### Generate Image
```bash
# POST request
curl -X POST http://localhost:5000/image/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "a cat on a skateboard"}' \
  --output image.png

# GET request
curl "http://localhost:5000/image/generate?prompt=a+cat+on+a+skateboard" \
  --output image.png
```

### Health Check
```bash
curl http://localhost:5000/ping
```

## License
Educational purposes.
