# Build stage
FROM pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-input --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV HF_HOME=/app/cache

RUN mkdir -p /app/cache && \
    useradd -m -u 1000 make && \
    chown -R make:make /app

USER make

EXPOSE 5000

CMD ["python", "main.py"]