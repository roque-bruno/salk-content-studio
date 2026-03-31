FROM python:3.13-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1

# Install system dependencies (ffmpeg for video assembler, curl for healthcheck)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg curl && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid 1000 --create-home appuser

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY src/ ./src/

# Copy pyproject.toml for editable install metadata
COPY pyproject.toml ./
RUN touch README.md && pip install --no-cache-dir -e .

# Create output directories with correct permissions
RUN mkdir -p /app/output/studio /app/output/video /app/output/logs /app/uploads /app/settings && \
    chown -R appuser:appuser /app/output /app/uploads /app/settings

# Switch to non-root user
USER appuser

# Environment
ENV PYTHONPATH=/app/src
ENV PORT=8000

EXPOSE ${PORT}

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/api/health')" || exit 1

# Run with 2 workers for production
CMD ["python", "-m", "uvicorn", "content_pipeline.web.app:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2"]
