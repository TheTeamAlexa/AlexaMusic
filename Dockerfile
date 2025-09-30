FROM python:3.12-slim

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    ffmpeg \
    git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./ 

RUN python3.12 -m pip install --upgrade pip && \
    python3.12 -m pip install --no-cache-dir --prefer-binary -r requirements.txt

COPY . .

CMD ["bash", "start"]
