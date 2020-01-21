# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory to /api
WORKDIR /ui

# Copy the current directory contents into the container at /api
ADD ./ /ui

# Install any needed packages specified in requirements.txt
RUN apk update
RUN apk add busybox-extras
RUN apk --update add gcc make g++ zlib-dev
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r /ui/requirements.txt

# Define environment variable
ENV PATH=$PATH:/ui/
ENV PYTHONPATH /ui/

# Run when the container launches
EXPOSE 3000
#CMD python /api/wsgi.py
CMD /ui/run.sh