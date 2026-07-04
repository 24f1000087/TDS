#!/bin/bash
# Start Redis server in the background
redis-server --daemonize yes

# Start Ollama server in the background
export OLLAMA_ORIGINS=*
ollama serve &

# Wait until Ollama is actually ready before FastAPI starts taking traffic,
# so the first real request isn't the one that has to wait on a cold start.
for i in $(seq 1 30); do
  if curl -s http://localhost:11434 >/dev/null 2>&1; then
    echo "Ollama is up"
    break
  fi
  sleep 1
done

# Start the FastAPI application on the port provided by Render (default 10000)
exec uvicorn main:app --host 0.0.0.0 --port ${PORT:-10000}
