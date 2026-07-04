FROM python:3.11-slim

# Install Redis and curl (curl is needed to fetch the Ollama install script)
RUN apt-get update && \
    apt-get install -y redis-server curl && \
    rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application code
COPY . .

# Make the start script executable
RUN chmod +x start.sh

# Bake the model into the image at build time, so the container doesn't
# need to download ~350MB over the network on every cold start.
RUN (ollama serve &) && \
    sleep 5 && \
    ollama pull qwen2.5:0.5b && \
    sleep 2

# Start the container
CMD ["./start.sh"]
