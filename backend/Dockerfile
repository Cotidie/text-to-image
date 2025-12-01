# Default to NVIDIA base image if not specified
#   - NVIDIA: pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime
#   - AMD: rocm/pytorch:rocm7.1_ubuntu24.04_py3.12_pytorch_release_2.8.0
ARG BASE_IMAGE=pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime
FROM ${BASE_IMAGE}

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/etc/cache
ENV MODEL_PATH=/etc/model
ENV PORT=5555

COPY requirements.txt requirements.txt
RUN pip install --no-input --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5555

CMD ["python", "main.py"]