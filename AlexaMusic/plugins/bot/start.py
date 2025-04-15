# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio

from pyrogram import filters
from pyrogram import enums, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from AlexaMusic import Telegram, YouTube, app
from AlexaMusic.misc import SUDOERS
from AlexaMusic.plugins.play.playlist import del_plist_msg
from AlexaMusic.plugins.sudo.sudoers import sudoers_list
from AlexaMusic.utils.database import (
    add_served_chat,
    is_served_user,
    add_served_user,
    blacklisted_chats,
    get_assistant,
    get_lang,
    get_userss,
    is_on_off,
    is_served_private_chat,
)
from AlexaMusic.utils.decorators.language import LanguageStart
from AlexaMusic.utils.inline import help_pannel, private_panel, start_pannel
from AlexaMusic.utils.command import commandpro

loop = asyncio.get_running_loop()


@app.on_message(
    filters.command(get_command("START_COMMAND")) & filters.private & ~BANNED_USERS
)
@LanguageStart
async def start_comm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            return await message.reply_text(_["help_1"], reply_markup=keyboard)
        if name[0:4] == "song":
            return await message.reply_text(_["song_2"])
        if name[0:3] == "sta":
            m = await message.reply_text(
                "🥱 Đang lấy thống kê cá nhân của bạn từ máy chủ {config.MUSIC_BOT_NAME}."
            )
            stats = await get_userss(message.from_user.id)
            tot = len(stats)
            if not stats:
                await asyncio.sleep(1)
                return await m.edit(_["ustats_1"])

            def get_stats():
                msg = ""
                limit = 0
                results = {}
                for i in stats:
                    top_list = stats[i]["spot"]
                    results[str(i)] = top_list
                    list_arranged = dict(
                        sorted(
                            results.items(),
                            key=lambda item: item[1],
                            reverse=True,
                        )
                    )
                if not results:
                    return m.edit(_["ustats_1"])
                tota = 0
                videoid = None
                for vidid, count in list_arranged.items():
                    tota += count
                    if limit == 10:
                        continue
                    if limit == 0:
                        videoid = vidid
                    limit += 1
                    details = stats.get(vidid)
                    title = (details["title"][:35]).title()
                    if vidid == "telegram":
                        msg += f"🔗[Telegram Media](https://t.me/Shayri_Music_Lovers) **đã phát {count} lần**\n\n"
                    else:
                        msg += f"🔗 [{title}](https://www.youtube.com/watch?v={vidid}) **đã phát {count} lần**\n\n"
                msg = _["ustats_2"].format(tot, tota, limit) + msg
                return videoid, msg

            try:
                videoid, msg = await loop.run_in_executor(None, get_stats)
            except Exception as e:
                print(e)
                return
            thumbnail = await YouTube.thumbnail(videoid, True)
            await m.delete()
            await message.reply_photo(photo=thumbnail, caption=msg)
            return
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} vừa khởi động bot để kiểm tra <code>danh sách sudo</code>\n\n**ID người dùng:** {sender_id}\n**Tên người dùng:** {sender_name}",
                )
            return
        if name[0:3] == "lyr":
            query = (str(name)).replace("lyrics_", "", 1)
            lyrical = config.lyrical
            lyrics = lyrical.get(query)
            if lyrics:
                return await Telegram.send_split_text(message, lyrics)
            else:
                return await message.reply_text("Không thể lấy được lời bài hát.")
        if name[0:3] == "del":
            await del_plist_msg(client=client, message=message, _=_)
        if name[0:3] == "inf":
            m = await message.reply_text("🔎 Đang tìm kiếm...")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
😲**Thông tin bài hát**😲

📌**Tiêu đề:** {title}

⏳**Thời lượng:** {duration} phút
👀**Lượt xem:** `{views}`
⏰**Ngày đăng:** {published}
🎥**Kênh:** {channel}
📎**Liên kết kênh:** [Xem kênh]({channellink})
🔗**Liên kết:** [Xem trên YouTube]({link})

💖 Tìm kiếm được cung cấp bởi {config.MUSIC_BOT_NAME}"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="• YouTube •", url=f"{link}"),
                        InlineKeyboardButton(text="• Đóng •", callback_data="close"),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode=enums.ParseMode.MARKDOWN,
                reply_markup=key,
            )
            if await is_on_off(config.LOG):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await app.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} vừa khởi động bot để kiểm tra <code>thông tin bài hát</code>\n\n**ID người dùng:** {sender_id}\n**Tên người dùng:** {sender_name}",
                )
    else:
        try:
            await app.resolve_peer(OWNER_ID[0])
            OWNER = OWNER_ID[0]
        except:
            OWNER = None
        out = private_panel(_, app.username, OWNER)
        if config.START_IMG_URL:
            try:
                await message.reply_photo(
                    photo=config.START_IMG_URL,
                    caption=_["start_2"].format(message.from_user.mention, app.mention),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            except:
                await message.reply_text(
                    caption=_["start_2"].format(message.from_user.mention, app.mention),
                    reply_markup=InlineKeyboardMarkup(out),
                )
        else:
            await message.reply_text(
                caption=_["start_2"].format(message.from_user.mention, app.mention),
                reply_markup=InlineKeyboardMarkup(out),
            )
        if await is_on_off(config.LOG):
            sender_id = message.from_user.id
            sender_name = message.from_user.first_name
            return await app.send_message(
                config.LOG_GROUP_ID,
                f"{message.from_user.mention} vừa khởi động bot của bạn.\n\n**ID người dùng:** {sender_id}\n**Tên người dùng:** {sender_name}",
            )


@app.on_message(
    filters.command(get_command("START_COMMAND")) & filters.group & ~BANNED_USERS
)
@LanguageStart
async def testbot(client, message: Message, _):
    out = start_pannel(_)
    return await message.reply_text(
        _["start_1"].format(message.chat.title, config.MUSIC_BOT_NAME),
        reply_markup=InlineKeyboardMarkup(out),
    )


welcome_group = 2


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(client, message: Message):
    chat_id = message.chat.id
    if config.PRIVATE_BOT_MODE == str(True):
        if not await is_served_private_chat(message.chat.id):
            await message.reply_text(
                "**Bot nhạc riêng tư**\n\nChỉ dành cho các nhóm được chủ sở hữu cho phép. Vui lòng liên hệ với chủ sở hữu của tôi để được cấp quyền cho nhóm của bạn. Nếu bạn không muốn làm vậy thì tôi sẽ rời khỏi nhóm."
            )
            return await app.leave_chat(message.chat.id)
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if member.id == app.id:
                chat_type = message.chat.type
                if chat_type != enums.ChatType.SUPERGROUP:
                    await message.reply_text(_["start_6"])
                    return await app.leave_chat(message.chat.id)
                if chat_id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_7"].format(
                            f"https://t.me/{app.username}?start=sudolist"
                        )
                    )
                    return await app.leave_chat(chat_id)
                userbot = await get_assistant(message.chat.id)
                out = start_pannel(_)
                await message.reply_text(
                    _["start_3"].format(
                        config.MUSIC_BOT_NAME,
                        userbot.username,
                        userbot.id,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
            if member.id in config.OWNER_ID:
                return await message.reply_text(
                    _["start_4"].format(config.MUSIC_BOT_NAME, member.mention)
                )
            if member.id in SUDOERS:
                return await message.reply_text(
                    _["start_5"].format(config.MUSIC_BOT_NAME, member.mention)
                )
            return
        except:
            return


@app.on_message(commandpro(["/alive", "minion"]))
async def alive(client, message: Message):
    await message.reply_photo(
        photo=f"https://i.ibb.co/CKyHh35V/Chat-GPT-Image-09-50-48-11-thg-4-2025.png",
        caption=f"""━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪ Xin chào, Minion đang hoạt động bình thường\n""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🌼 Nhóm Minion 💮", url=config.SUPPORT_GROUP)]]
        ),
    )


@app.on_message(commandpro(["/verify", "minionverify"]))
async def verify(client, message: Message):
    if await is_served_user(message.from_user.id):
        await message.reply_text(
            text="😂 Bạn đã được xác minh rồi",
        )
        return
    await add_served_user(message.from_user.id)
    await message.reply_photo(
        photo=f"https://i.ibb.co/CKyHh35V/Chat-GPT-Image-09-50-48-11-thg-4-2025.png",
        caption=f"""━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪ **Chúc mừng** 🎉\n✪ Bây giờ bạn là thành viên đã xác minh của Minion, hãy quay lại và tận hưởng dịch vụ của chúng tôi và phát nhạc 🌼 ..\n\n━━━━━━━━━━━━━━━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🌼 Nhóm Minion 💮", url=config.SUPPORT_GROUP)]]
        ),
    )
