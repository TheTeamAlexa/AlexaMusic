FROM python:3.11-bookworm

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
ENV PIP_NO_CACHE_DIR=1 PYTHONUNBUFFERED=1

RUN apt update && \
    apt upgrade -y && \
    apt install -y ffmpeg apt-utils build-essential python3-dev && \
    pip3 install -U pip wheel setuptools && \
    apt-get clean
    
COPY . .  

RUN pip3 install --no-cache-dir -U -r requirements.txt && \
    apt update && apt autoremove -y && \
    apt clean && rm -rf /var/lib/apt/lists/* ~/.thumbs/* ~/.cache

CMD python3 -m AlexaMusic
