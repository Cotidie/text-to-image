# Default to NVIDIA base image if not specified
# NVIDIA: pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime
# AMD: rocm7.1_ubuntu24.04_py3.12_pytorch_release_2.8.0
ARG BASE_IMAGE=pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime
FROM ${BASE_IMAGE}

WORKDIR /app

COPY . .
RUN pip install --no-input --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/app/cache
ENV PORT=5555

EXPOSE 5555

CMD ["python", "main.py"]