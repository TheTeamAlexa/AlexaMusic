#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alisha © Alexa © Yukki


from AlexaMusic import app
from AlexaMusic.utils.database import get_cmode


async def get_channeplayCB(_, command, CallbackQuery):
    if command == "c":
        chat_id = await get_cmode(CallbackQuery.message.chat.id)
        if chat_id is None:
            try:
                return await CallbackQuery.answer(_["setting_12"], show_alert=True)
            except:
                return
        try:
            chat = await app.get_chat(chat_id)
            channel = chat.title
        except:
            try:
                return await CallbackQuery.answer(_["cplay_4"], show_alert=True)
            except:
                return
    else:
        chat_id = CallbackQuery.message.chat.id
        channel = None
    return chat_id, channel
