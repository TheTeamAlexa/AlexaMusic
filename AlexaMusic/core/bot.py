# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import sys

from telethon import TelegramClient
from telethon.errors import ChatAdminRequiredError

import config

from ..logging import LOGGER


class AlexaBot(TelegramClient):
    def __init__(self):
        super().__init__(
            "AlexaMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            flood_sleep_threshold=180,
        )
        LOGGER(__name__).info(f"Starting Bot")

    async def start(self):
        await super().start(bot_token=config.BOT_TOKEN)
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = f"[{self.name}](tg://user?id={self.id})"
        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                text=f"<u><b>{self.mention} Bot Started :</b><u>\n\nId : <code>{self.id}</code>\nName : {self.name}\nUsername : @{self.username}",
                parse_mode="html",
            )
        except ChatAdminRequiredError:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted it as admin!"
            )
            sys.exit()
        try:
            a = await self.get_permissions(config.LOG_GROUP_ID, self.id)
            if not a.is_admin:
                LOGGER(__name__).error("Please promote bot as admin in logger group")
                sys.exit()
        except ValueError:
            LOGGER(__name__).error("Please promote bot as admin in logger group")
            sys.exit()
        except Exception:
            pass

        LOGGER(__name__).info(f"MusicBot started as {self.name}")
