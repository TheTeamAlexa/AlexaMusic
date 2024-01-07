# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from AlexaMusic import app
from AlexaMusic.core.call import Alexa
from AlexaMusic.utils.database import is_muted, mute_on
from AlexaMusic.utils.decorators import AdminRightsCheck

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(filters.command(MUTE_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"], disable_web_page_preview=True)
    await mute_on(chat_id)
    await Alexa.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention), disable_web_page_preview=True
    )
