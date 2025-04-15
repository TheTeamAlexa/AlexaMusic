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

import config
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.database.memorydatabase import get_video_limit
from AlexaMusic.utils.formatters import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text("Vui lòng đợi... Đang lấy thông tin cấu hình của bạn...")
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = "Not Configured"
    up_b = "Not Configured"
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "ʏᴇs"
    else:
        ass = "ɴᴏ"
    if config.PRIVATE_BOT_MODE == str(True):
        pvt = "ʏᴇs"
    else:
        pvt = "ɴᴏ"
    if config.AUTO_SUGGESTION_MODE == str(True):
        a_sug = "ʏᴇs"
    else:
        a_sug = "ɴᴏ"
    if config.AUTO_DOWNLOADS_CLEAR == str(True):
        down = "ʏᴇs"
    else:
        down = "ɴᴏ"

    git = "ɴᴏ"
    if not config.START_IMG_URL:
        start = "ɴᴏ"
    else:
        start = f"[ɪᴍᴀɢᴇ]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "ɴᴏ"
    else:
        s_c = f"[ᴄʜᴀɴɴᴇʟ]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "ɴᴏ"
    else:
        s_g = f"[sᴜᴩᴩᴏʀᴛ]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "ɴᴏ"
    else:
        token = "ʏᴇs"
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        sotify = "ɴᴏ"
    else:
        sotify = "ʏᴇs"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**THÔNG TIN CẤU HÌNH BOT NHẠC::**

**<u>CÁC BIẾN CƠ BẢN:</u>**
**TÊN BOT** : `{bot_name}`
**GIỚI HẠN THỜI LƯỢNG** : `{play_duration} phút`
**GIỚI HẠN TẢI NHẠC** : `{song} phút`
**ID ADMIN** : `{owner_id}`
    
**<u>THÔNG TIN KHO MÃ NGUỒN:</u>**
**UPSTREAM REPO** : `{up_r}`
**UPSTREAM BRANCH** : `{up_b}`
**GITHUB REPO** : `{git}`
**GIT TOKEN**: `{token}`


**<u>CẤU HÌNH BOT:</u>**
**TỰ ĐỘNG RỜI NHÓM** : `{ass}`
**THỜI GIAN RỜI NHÓM** : `{auto_leave} giây`
**CHẾ ĐỘ GỢI Ý TỰ ĐỘNG** : `{a_sug}`
**THỜI GIAN GỢI Ý** : `{auto_sug} giây`
**TỰ XÓA TẢI XUỐNG** : `{down}`
**CHẾ ĐỘ BOT RIÊNG TƯ** : `{pvt}`
**THỜI GIAN CHỜ YOUTUBE** : `{yt_sleep} giây`
**THỜI GIAN CHỜ TELEGRAM** : `{tg_sleep} giây`
**XÓA TIN NHẮN SAU** : `{cm} phút`
**GIỚI HẠN STREAM VIDEO** : `{v_limit} cuộc trò chuyện`
**GIỚI HẠN PLAYLIST MÁY CHỦ** : `{playlist_limit}`
**GIỚI HẠN LẤY PLAYLIST** : `{fetch_playlist}`

**<u>CẤU HÌNH SPOTIFY:</u>**
**SPOTIFY CLIENT ID** : `{sotify}`
**SPOTIFY CLIENT SECRET** : `{sotify}`

**<u>GIỚI HẠN KÍCH THƯỚC:</u>**
**GIỚI HẠN FILE AUDIO** : `{tg_aud}`
**GIỚI HẠN FILE VIDEO** : `{tg_vid}`

**<u>THÔNG TIN THÊM:</u>**
**KÊNH HỖ TRỢ** : `{s_c}`
**NHÓM HỖ TRỢ** : `{s_g}`
**ẢNH KHỞI ĐỘNG** : `{start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
