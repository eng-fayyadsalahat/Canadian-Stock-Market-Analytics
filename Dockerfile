FROM python:3.11-slim-bookworm

# Working Directory
WORKDIR /app

# Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install Dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy Project Files
COPY . .

# Create Required Directories
RUN mkdir -p data/processed outputs/logs

# Run Pipeline
CMD ["python", "run_pipeline.py"]