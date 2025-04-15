# Copyright (C) 2025 bởi Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Đăng ký kênh YouTube < Jankari Ki Duniya >. Bảo lưu tất cả quyền. © Alexa © Yukki.

"""
TheTeamAlexa là một dự án của các bot Telegram với nhiều mục đích khác nhau.
Bản quyền (c) 2021 ~ Hiện tại Team Alexa <https://github.com/TheTeamAlexa>

Chương trình này là phần mềm miễn phí: bạn có thể phân phối lại và sửa đổi
theo ý muốn hoặc có thể cộng tác nếu bạn có ý tưởng mới.
"""


from pyrogram import filters

import config
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS
from AlexaMusic.utils.database import autoend_off, autoend_on
from AlexaMusic.utils.decorators.language import language

# Lệnh
AUTOEND_COMMAND = get_command("AUTOEND_COMMAND")


@app.on_message(filters.command(AUTOEND_COMMAND) & SUDOERS)
async def auto_end_stream(client, message):
    usage = "**ᴜsᴀɢᴇ:**\n\n/autoend [enable|disable]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await autoend_on()
        await message.reply_text(
            "Kích hoạt tự động kết thúc stream.\n\nTrợ lý sẽ tự động rời khỏi cuộc gọi video sau vài phút nếu không có ai tham gia với lời nhắc nhở."
        )
    elif state == "disable":
        await autoend_off()
        await message.reply_text("Đã vô hiệu hóa tự động kết thúc stream.")
    else:
        await message.reply_text(usage)
