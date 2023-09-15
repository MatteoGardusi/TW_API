# Use the official Python image as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /TW_API

# Copy the application files into the working directory
COPY . /TW_API

# Install the application dependencies
RUN pip install -r requirements.txt

# Specifica il comando per eseguire il tuo script quando il contenitore viene avviato
CMD ["python", "app.py"]