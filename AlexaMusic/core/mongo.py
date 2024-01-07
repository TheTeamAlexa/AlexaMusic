# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config

from ..logging import LOGGER

TEMP_MONGODB = ""


if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning("No MONGO DB URL found.")
    temp_client = Client(
        "Alexa",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    mongodb = _mongo_async_.Alexa
    pymongodb = _mongo_sync_.Alexa

## Database For Broadcast Subscription By Team Alexa

MONGODB_CLI = MongoClient(config.MONGO_DB_URI)
db = MONGODB_CLI["subscriptions"]
