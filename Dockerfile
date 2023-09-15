
# Use a base image that includes Python (you can specify the desired version)
FROM python:3.11

# Create a working directory inside the container
WORKDIR /TW_API

# Copy your app.py file to the working directory of the container
COPY app.py .

# Create a virtual environment
RUN python -m venv venv

# Activate the virtual environment
# The original code has multiple issues:
# - The SHELL instruction should be placed before the RUN instruction that installs the virtual environment.
# - The "source" command cannot be used directly in the RUN instruction as it starts a new shell session every time.
# - To activate the virtual environment, we need to use the "venv/bin/activate" file as the shell script to run.
# - We can activate the virtual environment using the "source" command followed by the path to the "activate" file.
# - By using the "&&" operator, we can combine multiple commands into a single RUN instruction to minimize the number of layers created.
RUN . /TW_API/venv/bin/activate && \
    echo "Virtual environment activated."

# Install the dependencies of your script inside the virtual environment
# The original code correctly copies the requirements.txt file into the container.
# We use the "pip install" command to install the dependencies specified in the requirements.txt file.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Specify the command to run your script inside the virtual environment when the container starts
# The original code correctly specifies the command to run the app.py script using the Python interpreter.
CMD ["python", "app.py"]

# Expose the TCP port
EXPOSE 8000
