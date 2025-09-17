#!/bin/bash

# Production startup script
echo "Starting Financial Data Assistant..."

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Creating .env file from example..."
    cp .env.example .env
    echo "Please edit .env file with your OpenAI API key"
    exit 1
fi

# Build and start services
echo "Building and starting Docker containers..."
docker-compose up --build -d

# Wait for services to be healthy
echo "Waiting for services to be ready..."
sleep 10

# Check service health
echo "Checking service health..."
docker-compose ps

echo "Services started!"
echo "Frontend: http://localhost:8501"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "To stop services: docker-compose down"
echo "To view logs: docker-compose logs -f"
