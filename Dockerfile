# Base image with Python
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy app code
COPY app/ app/
COPY data/ data/
COPY main.py .

# Entrypoint
CMD ["python", "main.py"]
