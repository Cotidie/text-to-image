#!/bin/bash

# Stop script on error
set -e

# Configuration
REMOTE_USER="make"
REMOTE_HOST="makinteract.com"
REMOTE_PATH="/var/www/makinteract.com"

echo "🚀 Starting deployment..."

# 1. Build the project using Docker
# We use --rm to remove the container after it exits
echo "📦 Building frontend..."
docker compose run --rm --build builder

# 2. Copy files to remote server
echo "📤 Copying files to $REMOTE_HOST..."
scp -r dist/* "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"

echo "✅ Deployment complete!"