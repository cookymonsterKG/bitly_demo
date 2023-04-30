# Base image
FROM ubuntu:latest

# Update package lists
RUN apt-get update

# Install Python 3.11 and pip
RUN apt-get install -y python3.11 python3-pip

# Set Python 3.11 as the default Python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Set the working directory
WORKDIR /home

# Copy the application files to the container
COPY . /home


