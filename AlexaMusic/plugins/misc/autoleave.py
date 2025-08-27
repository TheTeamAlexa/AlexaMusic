# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import asyncio
from datetime import datetime
from pyrogram.enums import ChatType

import config
from AlexaMusic import app
from AlexaMusic.core.call import Alexa, autoend
from AlexaMusic.utils.database import (
    get_client,
    is_active_chat,
    is_autoend,
)

autoend = {}


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT != str(True):
        return
    while not await asyncio.sleep(config.AUTO_LEAVE_ASSISTANT_TIME):
        from AlexaMusic.core.userbot import assistants

        for num in assistants:
            client = await get_client(num)
            try:
                async for i in client.get_dialogs():
                    chat_type = i.chat.type
                    if chat_type in [
                        ChatType.SUPERGROUP,
                        ChatType.GROUP,
                        ChatType.CHANNEL,
                    ]:
                        chat_id = i.chat.id
                        if chat_id not in [
                            config.LOG_GROUP_ID,
                            -1001686672798,
                        ] and not await is_active_chat(chat_id):
                            try:
                                await client.leave_chat(chat_id)
                            except Exception:
                                continue
            except Exception:
                pass


asyncio.create_task(auto_leave())


# async def auto_end():
#     while not await asyncio.sleep(30):
#         if not await is_autoend():
#             continue
#         for chat_id in autoend:
#             timer = autoend.get(chat_id)
#             if not timer:
#                 continue
#             if datetime.now() > timer:
#                 if not await is_active_chat(chat_id):
#                     autoend[chat_id] = {}
#                     continue
#                 autoend[chat_id] = {}
#                 try:
#                     await Alexa.stop_stream(chat_id)
#                 except Exception:
#                     continue
#                 try:
#                     await app.send_message(
#                         chat_id,
#                         "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
#                     )
#                 except Exception:
#                     continue


# asyncio.create_task(auto_end())
