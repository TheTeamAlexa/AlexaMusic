# Copyright (C) 2025 bởi Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Đăng ký kênh YouTube < Jankari Ki Duniya >. Bảo lưu tất cả quyền. © Alexa © Yukki.

"""
TheTeamAlexa là một dự án của các bot Telegram với nhiều mục đích khác nhau.
Bản quyền (c) 2021 ~ Hiện tại Team Alexa <https://github.com/TheTeamAlexa>

Chương trình này là phần mềm miễn phí: bạn có thể phân phối lại và sửa đổi
theo ý muốn hoặc có thể cộng tác nếu bạn có ý tưởng mới.
"""

from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from strings import get_command
from AlexaMusic import app
from AlexaMusic.core.call import Alexa
from AlexaMusic.utils.decorators.play import PlayWrapper
from AlexaMusic.utils.logger import play_logs
from AlexaMusic.utils.stream.stream import stream

# Lệnh
STREAM_COMMAND = get_command("STREAM_COMMAND")


@app.on_message(filters.command(STREAM_COMMAND) & filters.group & ~BANNED_USERS)
@PlayWrapper
async def stream_command(
    client,
    message: Message,
    _,
    chat_id,
    video,
    channel,
    playmode,
    url,
    fplay,
):
    if url:
        mystic = await message.reply_text(
            _["play_2"].format(channel) if channel else _["play_1"]
        )
        try:
            await Alexa.stream_call(url)
        except NoActiveGroupCall:
            await mystic.edit_text(
                "Có vấn đề với bot. Vui lòng báo cáo cho chủ sở hữu của tôi và yêu cầu họ kiểm tra nhóm ghi log."
            )
            return await app.send_message(
                config.LOG_GROUP_ID,
                "Vui lòng bật cuộc gọi thoại.. Bot không thể phát URL.",
            )
        except Exception as e:
            return await mystic.edit_text(_["general_3"].format(type(e).__name__))
        await mystic.edit_text(_["str_2"])
        try:
            await stream(
                _,
                mystic,
                message.from_user.id,
                url,
                chat_id,
                message.from_user.first_name,
                message.chat.id,
                video=True,
                streamtype="index",
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = e if ex_type == "AssistantErr" else _["general_3"].format(ex_type)
            return await mystic.edit_text(err)
        return await play_logs(message, streamtype="M3u8 hoặc Liên kết Index")
    else:
        await message.reply_text(_["str_1"])
