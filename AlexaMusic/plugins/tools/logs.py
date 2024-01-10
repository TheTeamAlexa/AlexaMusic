# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from pyrogram import filters
from pyrogram.types import Message

from config import LOG_GROUP_ID
from AlexaMusic import app


@app.on_message(filters.new_chat_members)
async def new(_, message: Message):
    if app.id in [user.id for user in message.new_chat_members]:
        add = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        new = f"<b>✫ <u>ɴᴇᴡ ɢʀᴏᴜᴘ</u> :</b>\n\n<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>\n<b>ᴄʜᴀᴛ ᴛɪᴛʟᴇ :</b> {message.chat.title}\n\n<b>ᴀᴅᴅᴇᴅ ʙʏ :</b> {add} | <code>{message.from_user.id}</code>"
        await app.send_message(LOG_GROUP_ID, new)


@app.on_message(filters.left_chat_member)
async def left(_, message: Message):
    if app.id == message.left_chat_member.id:
        remove = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        left = f"<b>✫ <u>ʟᴇғᴛ ɢʀᴏᴜᴘ</u> :</b>\n\n<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>\n<b>ᴄʜᴀᴛ ᴛɪᴛʟᴇ :</b> {message.chat.title}\n\n<b>ʀᴇᴍᴏᴠᴇᴅ ʙʏ :</b> {remove} | <code>{message.from_user.id}</code>"
        await app.send_message(LOG_GROUP_ID, left)
