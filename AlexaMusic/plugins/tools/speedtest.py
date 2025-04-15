# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


async def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        await m.edit("<b>⇆ Đang chạy kiểm tra tốc độ tải xuống...</b>")
        test.download()
        await m.edit("<b>⇆ Đang chạy kiểm tra tốc độ tải lên...</b>")
        test.upload()
        test.results.share()
        result = test.results.dict()
        await m.edit("<b>↻ Đang chia sẻ kết quả kiểm tra tốc độ...</b>")
    except Exception as e:
        return await m.edit(str(e))
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("» Đang chạy kiểm tra tốc độ mạng...")
    result = await testspeed(m)
    output = f"""✯ <b>Kết Quả Kiểm Tra Tốc Độ</b> ✯

<u><b>Máy Khách:</b></u>
<b>» Nhà Mạng:</b> {result['client']['isp']}
<b>» Quốc Gia:</b> {result['client']['country']}

<u><b>Máy Chủ:</b></u>
<b>» Tên:</b> {result['server']['name']}
<b>» Quốc Gia:</b> {result['server']['country']}, {result['server']['cc']}
<b>» Nhà Tài Trợ:</b> {result['server']['sponsor']}
<b>» Độ Trễ:</b> {result['server']['latency']} 
<b>» Ping:</b> {result['ping']}
"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
