# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install ffmpeg
RUN apt-get update -y && apt-get install ffmpeg -y

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any required dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Python script
CMD ["python", "./audio_downloader.py"]
