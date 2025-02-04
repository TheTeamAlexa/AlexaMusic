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
        await m.edit("<b>⇆ 𝖱𝗎𝗇𝗇𝗂𝗇𝗀 𝖣𝗈𝗐𝗅𝗈𝖺𝖽 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 ...</b>")
        test.download()
        await m.edit("<b>⇆ 𝖱𝗎𝗇𝗇𝗂𝗇𝗀 𝖴𝗉𝗅𝗈𝖺𝖽 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 ...</b>")
        test.upload()
        test.results.share()
        result = test.results.dict()
        await m.edit("<b>↻ 𝖲𝗁𝖺𝗋𝗂𝗇𝗀 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 𝖱𝖾𝗌𝗎𝗅𝗍𝗌 ...</b>")
    except Exception as e:
        return await m.edit(str(e))
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("» 𝖱𝗎𝗇𝗇𝗂𝗇𝗀 𝖠 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 ...")
    result = await testspeed(m)
    output = f"""✯ <b>𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 𝖱𝖾𝗌𝗎𝗅𝗍𝗌</b> ✯

<u><b>𝖢𝗅𝗂𝖾𝗇𝗍 :</b></u>
<b>» 𝖨𝖲𝖯 :</b> {result['client']['isp']}
<b>» 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 :</b> {result['client']['country']}

<u><b>𝖲𝖾𝗋𝗏𝖾𝗋 :</b></u>
<b>» 𝖭𝖺𝗆𝖾 :</b> {result['server']['name']}
<b>» 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 :</b> {result['server']['country']}, {result['server']['cc']}
<b>» 𝖲𝗉𝗈𝗇𝗌𝗈𝗋 :</b> {result['server']['sponsor']}
<b>» 𝖫𝖺𝗍𝖾𝗇𝖼𝗒 :</b> {result['server']['latency']} 
<b>» 𝖯𝗂𝗇𝗀 :</b> {result['ping']}
"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
