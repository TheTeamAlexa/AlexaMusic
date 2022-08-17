# Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma


import asyncio
import os
import shutil
from sys import version as pyver

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS
from config import BOT_ID, MUSIC_BOT_NAME, OWNER_ID
from AlexaMusic.utils.database import (
    add_gban_user,
    get_served_chats,
    get_sudoers,
    is_gbanned_user,
    remove_gban_user,
)


## Gban Module


@app.on_message(filters.command("gban") & SUDOERS)
async def ban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            await message.reply_text("**Usage:**\n/gban [USERNAME | USER_ID]")
            return
        user = message.text.split(None, 2)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id == from_user.id:
            return await message.reply_text("You want to gban yourself? How Fool!")
        elif user.id in SUDOERS:
            await message.reply_text("You want to block a sudo user? KIDXZ")
        else:
            await add_gban_user(user.id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**Alexa Is Initializing Global Ban on {user.mention}**\n\nExpected Time : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.ban_chat_member(sex, user.id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
__**New Global Ban on {MUSIC_BOT_NAME}**__

**Origin:** {message.chat.title} [`{message.chat.id}`]
**Sudo User:** {from_user.mention}
**Banned User:** {user.mention}
**Banned User ID:** `{user.id}`
**Chats:** {number_of_chats}"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
        return
    from_user_id = message.from_user.id
    from_user_mention = message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    sudoers = await get_sudoers()
    if user_id == from_user_id:
        await message.reply_text("You want to block yourself? How Fool!")
    elif user_id in sudoers:
        await message.reply_text("You want to block a sudo user? KIDXZ")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if is_gbanned:
            await message.reply_text("Already Gbanned.")
        else:
            await add_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**Alexa Is Initializing Gobal Ban on {mention}**\n\nExpected Time : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.ban_chat_member(sex, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
__**New Global Ban on {MUSIC_BOT_NAME}**__

**Origin:** {message.chat.title} [`{message.chat.id}`]
**Sudo User:** {from_user_mention}
**Banned User:** {mention}
**Banned User ID:** `{user_id}`
**Chats:** {number_of_chats}"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
            return


@app.on_message(filters.command("ungban") & SUDOERS)
async def unban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text("**Usage:**\n/ungban [USERNAME | USER_ID]")
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        sudoers = await get_sudoers()
        if user.id == from_user.id:
            await message.reply_text("You want to unblock yourself?")
        elif user.id in sudoers:
            await message.reply_text("Sudo users can't be blocked/unblocked.")
        else:
            is_gbanned = await is_gbanned_user(user.id)
            if not is_gbanned:
                await message.reply_text("He's already free, why bully him?")
            else:
                await remove_gban_user(user.id)
                await message.reply_text(f"Ungbanned!")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    sudoers = await get_sudoers()
    if user_id == from_user_id:
        await message.reply_text("You want to unblock yourself?")
    elif user_id in sudoers:
        await message.reply_text("Sudo users can't be blocked/unblocked.")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if not is_gbanned:
            await message.reply_text("He's already free, why bully him?")
        else:
            await remove_gban_user(user_id)
            await message.reply_text(f"Ungbanned!")


# Broadcast Message


@app.on_message(filters.command("bcast_pin") & SUDOERS)
async def broadcast_message_pin_silent(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"**Broadcasted Message In {sent}  Chats with {pin} Pins.**"
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**Usage**:\n/bcast_pin [MESSAGE] or [Reply to a Message]"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            try:
                await m.pin(disable_notification=True)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"**Broadcasted Message In {sent} Chats and {pin} Pins.**")


@app.on_message(filters.command("bcast_pin_loud") & SUDOERS)
async def broadcast_message_pin_loud(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=False)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"**Broadcasted Message In {sent}  Chats with {pin} Pins.**"
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**Usage**:\n/bcast_pin_loud [MESSAGE] or [Reply to a Message]"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            try:
                await m.pin(disable_notification=False)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"**Broadcasted Message In {sent} Chats and {pin} Pins.**")


@app.on_message(filters.command("bcast") & SUDOERS)
async def broadcast(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"**Broadcasted Message In {sent} Chats.**")
        return
    if len(message.command) < 2:
        await message.reply_text("**Usage**:\n/bcast [MESSAGE] or [Reply to a Message]")
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"**Broadcasted Message In {sent} Chats.**")


# Clean


@app.on_message(filters.command("clean") & SUDOERS)
async def clean(_, message):
    dir = "downloads"
    dir1 = "cache"
    shutil.rmtree(dir)
    shutil.rmtree(dir1)
    os.mkdir(dir)
    os.mkdir(dir1)
    await message.reply_text("Successfully cleaned all **temp** dir(s)!")
