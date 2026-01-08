# Use the official Python image
FROM python:3.12-slim-bookworm

# 1. Install uv binary directly
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# 2. Set the working directory
WORKDIR /app

# 3. CRITICAL: Add the virtual environment to the system PATH
# This allows the container to find 'uvicorn' automatically
ENV PATH="/app/.venv/bin:$PATH"

# 4. Copy dependency files first
COPY pyproject.toml uv.lock ./

# 5. Install dependencies into /app/.venv
RUN uv sync --frozen --no-cache

# 6. Copy your application files (predict.py and model.bin)
COPY predict.py model.bin ./

# 7. Expose the default Render port
EXPOSE 10000

# 8. Start command using uvicorn
# We use port 10000 to match Render's default expectations
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "10000"]
