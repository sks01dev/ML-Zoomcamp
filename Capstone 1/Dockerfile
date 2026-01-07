# Use the base Python image
FROM python:3.11-slim

# CRITICAL FIXES FOR WSL2/DOCKER DESKTOP
# Use copy mode instead of hard links to prevent SIGBUS/filesystem errors
ENV UV_LINK_MODE=copy
# Ensure uv does not try to use system environment configuration
ENV UV_PROJECT_ENVIRONMENT=""

WORKDIR /app

# Install uv using pip install is necessary for this specific workflow
RUN pip install --no-cache-dir uv

# Copy dependency definitions only
COPY pyproject.toml uv.lock ./

# Install locked dependencies into the default virtual environment in /app
# Note: --locked is correct here to ensure exact version matching
RUN uv sync --locked

# Copy ONLY required runtime files
COPY predict.py model.bin feature_columns.bin ./

EXPOSE 8000

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]
