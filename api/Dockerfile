# Use an official Python runtime as a parent image
FROM python:3.8-alpine

# Set the working directory to /api
WORKDIR /api

# Copy the current directory contents into the container at /api
ADD ./ /api

# Install any needed packages specified in requirements.txt
RUN apk update
RUN apk add busybox-extras
RUN apk --update add gcc make g++ zlib-dev
RUN pip install --upgrade pip
RUN pip install --trusted-host pypi.python.org -r /api/requirements.txt


# Define environment variable
ENV PATH=$PATH:/api/
ENV PYTHONPATH /api/

# Run when the container launches
EXPOSE 5000
#CMD python /api/wsgi.py
CMD /api/run.sh