# Start from a Python base image
FROM python:3.9-slim

# Set a working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY audio_downloader.py .

# Command to run the application
CMD ["python", "audio_downloader.py"]
