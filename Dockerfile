FROM python:3.12-bookworm

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends ffmpeg git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements.txt && \
    chmod +x start

CMD ["bash", "-c", "gunicorn app:app & exec bash start"]
