FROM python:3.11-slim

WORKDIR /app

# Copy project configuration first (for better caching)
COPY pyproject.toml VERSION README.md ./

# Copy source code
COPY src/ ./src/

# Install the package
RUN pip install --no-cache-dir -e .

# Copy web files
COPY index.html pyscript.toml ./

# Expose port
EXPOSE 8000

# Run simple HTTP server to serve the PyScript app
CMD ["python3", "-m", "http.server", "8000"]