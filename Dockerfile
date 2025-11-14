# Build stage
FROM pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime AS builder

WORKDIR /build

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --target=/install -r requirements.txt

# Runtime stage
FROM pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime

WORKDIR /app

# Copy only installed packages
COPY --from=builder /install /usr/local/lib/python3.10/site-packages/

# Copy application
COPY backend/ ./backend/
COPY main.py .

ENV PYTHONUNBUFFERED=1
ENV TRANSFORMERS_CACHE=/app/cache
ENV HF_HOME=/app/cache

RUN mkdir -p /app/cache && \
    useradd -m -u 1000 make && \
    chown -R make:make /app

USER make

EXPOSE 5000

CMD ["python", "main.py"]