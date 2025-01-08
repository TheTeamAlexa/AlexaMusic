FROM python:3.12-bookworm

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -U -r requirements.txt

COPY . .

CMD ["bash", "start"]
