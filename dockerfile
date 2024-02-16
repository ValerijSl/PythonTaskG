FROM python:3.10.4

# Set the working directory in the container to /app
WORKDIR /app

COPY . /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
