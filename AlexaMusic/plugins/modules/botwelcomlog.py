# This code is written by (C) TheTeamAlexa bot will send message to log group when someone add
# this bot to new group make sure to star all projects
# Copyright (C) 2021-2025 by Alexa_Help@ Github, < TheTeamAlexa >.
# All rights reserved. © Alexa © Yukki

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import LOG, LOG_GROUP_ID
from AlexaMusic import app
from AlexaMusic.utils.database import delete_served_chat, get_assistant, is_on_off


@app.on_message(filters.new_chat_members)
async def bot_added(_, message):
    try:
        if not await is_on_off(LOG):
            return
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = message.chat.username or "Private Chat"
                msg = (
                    f"<b>Bot added in</b> {message.chat.title}\n\n"
                    f"<b>Name:</b> {message.chat.title}\n"
                    f"<b>Id:</b> {message.chat.id}\n"
                    f"<b>Username:</b> @{username}\n"
                    f"<b>Added By:</b> {message.from_user.mention}"
                )
                await app.send_message(
                    LOG_GROUP_ID,
                    text=msg,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton(
                                    text=f"Added by: {message.from_user.first_name}",
                                    user_id=message.from_user.id,
                                )
                            ]
                        ]
                    ),
                )
                if message.chat.username:
                    await userbot.join_chat(message.chat.username)
    except Exception:
        pass


@app.on_message(filters.left_chat_member)
async def bot_kicked(_, message: Message):
    try:
        if not await is_on_off(LOG):
            return
        userbot = await get_assistant(message.chat.id)
        left_chat_member = message.left_chat_member
        if left_chat_member and left_chat_member.id == app.id:
            remove_by = (
                message.from_user.mention if message.from_user else "Unknown User"
            )
            title = message.chat.title
            username = (
                f"@{message.chat.username}" if message.chat.username else "Private Chat"
            )
            chat_id = message.chat.id
            left = (
                f"Bot was Removed in {title}\n"
                f"<b>Name</b>: {title}\n"
                f"<b>Id</b>: {chat_id}\n"
                f"<b>Username</b>: {username}\n"
                f"<b>Removed By</b>: {remove_by}"
            )

            await app.send_message(
                LOG_GROUP_ID,
                text=left,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text=f"Removed By: {message.from_user.first_name}",
                                user_id=message.from_user.id,
                            )
                        ]
                    ]
                ),
            )
            await delete_served_chat(chat_id)
            await userbot.leave_chat(chat_id)
    except Exception as e:
        pass
