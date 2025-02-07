FROM python:3.12-bookworm

# Update, upgrade, install dependencies, and clean up in one layer
RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends ffmpeg git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory and copy application files
WORKDIR /app
COPY . .

# Install Python dependencies without cache
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Start the application using gunicorn and the Python script concurrently.
CMD gunicorn app:app & bash start
