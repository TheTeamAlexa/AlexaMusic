# PM Protection

from protector.protector import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User
from config import MUSIC_BOT_NAME


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "✪ **ʜᴇʟʟᴏ, ɪ ᴀᴍ** {MUSIC_BOT_NAME}'s ᴀssɪsᴛᴀɴᴛ.\n\n✪ **ɪ ᴀᴍ ᴏɴʟʏ ᴀssɪsᴛᴀɴᴛ ᴅᴏ ɴᴏᴛ sᴘᴀᴍ ʜᴇʀᴇ ᴏᴛʜᴇʀᴡɪsᴇ ɪ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ʙʟᴏᴄᴋ ʏᴏᴜ** 😔🥰.\n**✪ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ᴏʀ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ ᴛʜᴇɴ ᴊᴏɪɴ** @Alexa_Help",
    )
    return
