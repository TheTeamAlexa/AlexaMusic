# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import sys
from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel
from telethon.errors import ChatAdminRequiredError
import config
from ..logging import LOGGER


class AlexaBot(TelegramClient):
    def __init__(self):
        super().__init__("MusicBot", api_id=config.API_ID, api_hash=config.API_HASH)
        self.bot_token = config.BOT_TOKEN
        self.username = None
        self.id = None
        self.name = None
        LOGGER(__name__).info(f"Starting Bot...")

    async def start(self):
        await super().start(bot_token=self.bot_token)
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        try:
            await self.send_message(
                PeerChannel(config.LOG_GROUP_ID),
                "» ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ, ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴀssɪsᴛᴀɴᴛ...",
            )
        except ChatAdminRequiredError:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted it as admin!"
            )
            sys.exit()
        participant = await self.get_participant(config.LOG_GROUP_ID, self.id)
        if not participant.is_admin:
            LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            sys.exit()
        LOGGER(__name__).info(f"MusicBot Started as {self.name}")
