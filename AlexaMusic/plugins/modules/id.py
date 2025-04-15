# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

from AlexaMusic import app
from pyrogram import filters


@app.on_message(filters.command("id"))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ID của bạn**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ID**: `{reply.from_user.id}`\n**Chat ID**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ID của bạn**: `{message.from_user.id}`\n**Chat ID**: `{message.chat.id}`"
        )
