# docker build -t makelab/text-to-image:local -f docker/local-Dockerfile .
FROM pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --no-input --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/app/cache
ENV PORT=5555

COPY backend/ .

USER make

EXPOSE 5555

CMD ["python", "main.py"]