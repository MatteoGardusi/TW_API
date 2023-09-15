
# Use a base image that includes Python (you can specify desired the version)
FROM python:3.11

# Create a working directory inside the container
WORKDIR /TW_API

# Copy your app.py file to the working directory of the container
COPY app.py .

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment
# Move the SHELL instruction before the RUN instruction that installs the virtual environment
# Activate the virtual environment using the "venv/bin/activate" file as the shell script to run
# Combine multiple commands into a single RUN instruction to minimize the number of layers created
SHELL ["/bin/bash", "-c"]
RUN source venv/bin/activate && \
    echo "Virtual environment activated."

# Install the dependencies of your script inside the virtual environment
# Copy the requirements.txt file into the container
# Use the "pip install" command to install the dependencies specified in the requirements.txt file
COPY requirements.txt .
RUN pip install -r requirements.txt

# Specify the command to run your script inside the virtual environment when the container starts
# Use the Python interpreter to run the app.py script
CMD ["python", "app.py"]

# Expose a TCP port for the container
# Add the EXPOSE instruction to specify the port to be exposed
EXPOSE 8000

# Define the entry point for the container
# Remove the second CMD instruction, as it conflicts with the previous CMD instruction
# Keep only one CMD instruction to define the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
