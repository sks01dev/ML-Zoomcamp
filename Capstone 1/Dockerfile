FROM python:3.12.1-slim-bookworm

# Install uv by copying it directly from its container image (much faster and smaller than pip)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Install uv (the fast package manager)
RUN pip install uv

# Set the working directory
WORKDIR /app

# Add the virtual environment’s bin directory to PATH so Python tools work globally

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies from the lock file
RUN uv sync --frozen --no-cache

# Copy the FastAPI app and model
COPY predict.py model.bin ./

# Expose port (optional but good practice)
EXPOSE 9696

# Start the FastAPI app with uvicorn
ENTRYPOINT ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
