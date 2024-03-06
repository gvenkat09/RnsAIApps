# Use the official lightweight Python image.
# https://hub.docker.com/_/python
# FROM python:3.8-slim
FROM python:3.12.2

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY . .

# Streamlit runs on port 8501 by default, expose this port
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "Homepage.py"]