#
# Copyright (C) 2021-2022 by Alexsacei@Github, < https://github.com/kenta9900 >.
# A Powerful Music Bot Property Of Rocks Indian NIRVANA

# Kanged By © @exsaezz
# Rocks © @groupjawanusantara
# Owner Alexsacei
# Alexsacei
# All rights reserved. © Alisha © Alexa © Yukki © Alexsacei


import logging
from logging.handlers import RotatingFileHandler

from config import LOG_FILE_NAME

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=5000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
