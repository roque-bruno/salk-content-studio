FROM python:3.11-slim

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

# Copy project files
COPY pyproject.toml ./
# README.md is optional for pip install
RUN touch README.md
COPY src/ ./src/

# Install dependencies
RUN pip install --no-cache-dir -e .

# Create output directories with correct permissions
RUN mkdir -p /app/output/studio /app/output/video /app/output/logs && \
    chown -R appuser:appuser /app/output

# Switch to non-root user
USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8080/api/health || exit 1

CMD ["uvicorn", "content_pipeline.web.app:app", "--host", "0.0.0.0", "--port", "8080"]
