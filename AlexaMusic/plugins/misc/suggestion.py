# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import random
from datetime import datetime, timedelta

import config
from config import clean
from strings import get_string
from AlexaMusic import app
from AlexaMusic.utils.database import (
    get_lang,
    get_private_served_chats,
    get_served_chats,
    is_suggestion,
)

LEAVE_TIME = config.AUTO_SUGGESTION_TIME


suggestor = {}

strings = [item for item in get_string("en") if item[:3] == "sug" and item != "sug_0"]


async def dont_do_this():
    if config.AUTO_SUGGESTION_MODE != str(True):
        return
    while not await asyncio.sleep(LEAVE_TIME):
        try:
            chats = []
            if config.PRIVATE_BOT_MODE == str(True):
                schats = await get_private_served_chats()
            else:
                schats = await get_served_chats()
            for chat in schats:
                chats.append(int(chat["chat_id"]))
            total = len(chats)
            if total >= 100:
                total //= 10
            send_to = 0
            random.shuffle(chats)
            for x in chats:
                if send_to == total:
                    break
                if x == config.LOG_GROUP_ID:
                    continue
                if not await is_suggestion(x):
                    continue
                try:
                    language = await get_lang(x)
                    _ = get_string(language)
                except Exception:
                    _ = get_string("en")
                string = random.choice(strings)
                if previous := suggestor.get(x):
                    while previous == (string.split("_")[1]):
                        string = random.choice(strings)
                suggestor[x] = string.split("_")[1]
                try:
                    msg = _["sug_0"] + _[string]
                    sent = await app.send_message(x, msg)
                    if x not in clean:
                        clean[x] = []
                    time_now = datetime.now()
                    put = {
                        "msg_id": sent.message_id,
                        "timer_after": time_now
                        + timedelta(minutes=config.CLEANMODE_DELETE_MINS),
                    }
                    clean[x].append(put)
                    send_to += 1
                except Exception:
                    pass
        except Exception:
            pass


asyncio.create_task(dont_do_this())
