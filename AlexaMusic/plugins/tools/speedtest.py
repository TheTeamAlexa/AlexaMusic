#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Dr_Asad_Ali
# Rocks © @Shayri_Music_Lovers
# Owner Asad Ali
# Harshit Sharma
# All rights reserved. © Alexa © Yukki


import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from AlexaMusic import app
from AlexaMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("🙄 ᴄʜᴇᴄᴋɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅ...")
        test.download()
        m = m.edit("🙄 ᴄʜᴇᴄᴋɪɴɢ ᴜᴩʟᴏᴀᴅ sᴩᴇᴇᴅ...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("😴 ᴜᴩʟᴏᴀᴅɪɴɢ sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs...")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("💫 ᴛʀʏɪɴɢ ᴛᴏ ᴄʜᴇᴄᴋ ᴜᴩʟᴏᴀᴅ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅ")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴩᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛs**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**__ɪsᴩ:__** {result['client']['isp']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ:**</u>
**__ɴᴀᴍᴇ:__** {result['server']['name']}
**__ᴄᴏᴜɴᴛʀʏ:__** {result['server']['country']}, {result['server']['cc']}
**__sᴩᴏɴsᴏʀ:__** {result['server']['sponsor']}
**__ʟᴀᴛᴇɴᴄʏ:__** {result['server']['latency']}  
**__ᴩɪɴɢ:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
