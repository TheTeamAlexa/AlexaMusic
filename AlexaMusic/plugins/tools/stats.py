import asyncio
import platform
from sys import version as pyver

import psutil
from pyrogram import __version__ as pyrover
from pyrogram import filters
from pyrogram.errors import MessageIdInvalid
from pyrogram.types import CallbackQuery, InputMediaPhoto, Message
from pytgcalls.__version__ import __version__ as pytgver

import config
from config import BANNED_USERS, MUSIC_BOT_NAME
from strings import get_command
from AlexaMusic import YouTube, app
from AlexaMusic.core.userbot import assistants
from AlexaMusic.misc import SUDOERS, pymongodb
from AlexaMusic.plugins import ALL_MODULES
from AlexaMusic.utils.database import (
    get_global_tops,
    get_particulars,
    get_queries,
    get_served_chats,
    get_served_users,
    get_sudoers,
    get_top_chats,
    get_topp_users,
)
from AlexaMusic.utils.decorators.language import language, languageCB
from AlexaMusic.utils.inline.stats import (
    back_stats_buttons,
    back_stats_markup,
    get_stats_markup,
    overallback_stats_markup,
    stats_buttons,
    top_ten_stats_markup,
)

loop = asyncio.get_running_loop()

# Commands
GSTATS_COMMAND = get_command("GSTATS_COMMAND")
STATS_COMMAND = get_command("STATS_COMMAND")

@app.on_message(
    filters.command(STATS_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def stats_global(client, message: Message, _):
    upl = stats_buttons(_, True if message.from_user.id in SUDOERS else False)
    await message.reply_photo(
        photo=config.STATS_IMG_URL,
        caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
        reply_markup=upl,
    )

@app.on_message(
    filters.command(GSTATS_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def gstats_global(client, message: Message, _):
    mystic = await message.reply_text(_["gstats_1"])
    stats = await get_global_tops()
    if not stats:
        await asyncio.sleep(1)
        return await mystic.edit(_["gstats_2"])

    def get_stats():
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
            return mystic.edit(_["gstats_2"])
        videoid = None
        co = None
        for vidid, count in list_arranged.items():
            if vidid == "telegram":
                continue
            else:
                videoid = vidid
                co = count
            break
        return videoid, co

    try:
        videoid, co = await loop.run_in_executor(None, get_stats)
    except Exception as e:
        print(e)
        return
    (
        title,
        duration_min,
        duration_sec,
        thumbnail,
        vidid,
    ) = await YouTube.details(videoid, True)
    title = title.title()
    final = f"Top Most Played Track on {MUSIC_BOT_NAME}\n\n**Title:** {title}\n\nPlayed** {co} **times"
    upl = get_stats_markup(_, True if message.from_user.id in SUDOERS else False)
    await app.send_photo(
        message.chat.id,
        photo=thumbnail,
        caption=final,
        reply_markup=upl,
    )
    await mystic.delete()

# Callback query for getting top users for a particular type
@app.on_callback_query(filters.regex("GetStatsNow") & ~BANNED_USERS)
@languageCB
async def top_users_ten(client, CallbackQuery: CallbackQuery, _):
    chat_id = CallbackQuery.message.chat.id
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    upl = back_stats_markup(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.edit_message_text(
        _["gstats_3"].format(
            f"of {CallbackQuery.message.chat.title}" if what == "Here" else what
        )
    )
    if what == "Tracks":
        stats = await get_global_tops()
    elif what == "Chats":
        stats = await get_top_chats()
    elif what == "Users":
        stats = await get_topp_users()
    elif what == "Here":
        stats = await get_particulars(chat_id)
    if not stats:
        await asyncio.sleep(1)
        return await mystic.edit(_["gstats_2"], reply_markup=upl)
    queries = await get_queries()

    def get_stats():
        results = {}
        for i in stats:
            top_list = stats[i] if what in ["Chats", "Users"] else stats[i]["spot"]
            results[str(i)] = top_list
            list_arranged = dict(
                sorted(
                    results.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )
        if not results:
            return mystic.edit(_["gstats_2"], reply_markup=upl)
        msg = ""
        limit = 0
        total_count = 0
        if what in ["Tracks", "Here"]:
            for items, count in list_arranged.items():
                total_count += count
                if limit == 10:
                    continue
                limit += 1
                details = stats.get(items)
                title = (details["title"][:35]).title()
                if items == "telegram":
                    msg += f"🔗 [ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs ᴀɴᴅ ᴀᴜᴅɪᴏs](https://t.me/Shayri_Music_Lovers) ** ᴘʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs**\n\n"
                else:
                    msg += f"🔗 [{title}](https://www.youtube.com/watch?v={items}) ** ᴘʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs**\n\n"

            temp = (
                _["gstats_4"].format(
                    queries,
                    config.MUSIC_BOT_NAME,
                    len(stats),
                    total_count,
                    limit,
                )
                if what == "Tracks"
                else _["gstats_7"].format(len(stats), total_count, limit)
            )
            msg = temp + msg
        return msg, list_arranged

    try:
        msg, list_arranged = await loop.run_in_executor(None, get_stats)
    except Exception as e:
        print(e)
        return
    limit = 0
    if what in ["Users", "Chats"]:
        for items, count in list_arranged.items():
            if limit == 10:
                break
            try:
                extract = (
                    (await app.get_users(items)).first_name
                    if what == "Users"
                    else (await app.get_chat(items)).title
                )
                if extract is None:
                    continue
                await asyncio.sleep(0.5)
            except:
                continue
            limit += 1
            msg += f"🔗`{extract}` ᴘʟᴀʏᴇᴅ {count} ᴛɪᴍᴇs ᴏɴ ʙᴏᴛ.\n\n"
        temp = (
            _["gstats_5"].format(limit, MUSIC_BOT_NAME)
            if what == "Chats"
            else _["gstats_6"].format(limit, MUSIC_BOT_NAME)
        )
        msg = temp + msg
    med = InputMediaPhoto(media=config.GLOBAL_IMG_URL, caption=msg)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(photo=config.GLOBAL_IMG_URL, caption=msg, reply_markup=upl)

@app.on_callback_query(filters.regex("TopOverall") & ~BANNED_USERS)
@languageCB
async def overall_stats(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"])
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(SUDOERS)
    mod = len(ALL_MODULES)
    assistant = len(assistants)
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    if config.AUTO_LEAVING_ASSISTANT == str(True):
        ass = "Yes"
    else:
        ass = "No"
    cm = config.CLEANMODE_DELETE_MINS
    text = f"""**ʙᴏᴛ's sᴛᴀᴛs ᴀɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ:**

**ɪᴍᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇs:** {mod}
**sᴇʀᴠᴇᴅ ᴄʜᴀᴛs:** {served_chats} 
**sᴇʀᴠᴇᴅ ᴜsᴇʀs:** {served_users} 
**ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs:** {blocked} 
**sᴜᴅᴏ ᴜsᴇʀs:** {sudoers} 
    
**ᴛᴏᴛᴀʟ ǫᴜᴇʀɪᴇs:** {total_queries} 
**ᴛᴏᴛᴀʟ ᴀssɪsᴛᴀɴᴛs:** {assistant}
**ᴀᴜᴛᴏ ʟᴇᴀᴠɪɴɢ ᴀssɪsᴛᴀɴᴛ:** {ass}
**ᴄʟᴇᴀɴᴍᴏᴅᴇ ᴅᴜʀᴀᴛɪᴏɴ:** {cm} Mins

**ᴘʟᴀʏ ᴅᴜʀᴀᴛɪᴏɴ ʟɪᴍɪᴛ:** {play_duration} Mins
**sᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪᴍɪᴛ:** {song} Mins
**ʙᴏᴛ's sᴇʀᴠᴇʀ ᴘʟᴀʏʟɪsᴛ Limit:** {playlist_limit}
**ᴘʟᴀʏʟɪsᴛ ᴘʟᴀʏ ʟɪᴍɪᴛ:** {fetch_playlist}"""
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(photo=config.STATS_IMG_URL, caption=text, reply_markup=upl)

# Callback query for getting sudo user stats
@app.on_callback_query(filters.regex("bot_stats_sudo"))
@languageCB
async def overall_stats(client, CallbackQuery, _):
    if CallbackQuery.from_user.id not in SUDOERS:
        return await CallbackQuery.answer("ᴏɴʟʏ ғᴏʀ sᴜᴅᴏ ᴜsᴇʀs", show_alert=True)
    callback_data = CallbackQuery.data.strip()
    what = callback_data.split(None, 1)[1]
    if what != "s":
        upl = overallback_stats_markup(_)
    else:
        upl = back_stats_buttons(_)
    try:
        await CallbackQuery.answer()
    except:
        pass
    await CallbackQuery.edit_message_text(_["gstats_8"])
    sc = platform.system()
    p_core = psutil.cpu_count(logical=False)
    t_core = psutil.cpu_count(logical=True)
    ram = str(round(psutil.virtual_memory().total / (1024.0**3))) + " GB"
    try:
        cpu_freq = psutil.cpu_freq().current
        if cpu_freq >= 1000:
            cpu_freq = f"{round(cpu_freq / 1000, 2)}GHz"
        else:
            cpu_freq = f"{round(cpu_freq, 2)}MHz"
    except:
        cpu_freq = "Unable to Fetch"
    hdd = psutil.disk_usage("/")
    total = hdd.total / (1024.0**3)
    total = str(total)
    used = hdd.used / (1024.0**3)
    used = str(used)
    free = hdd.free / (1024.0**3)
    free = str(free)
    mod = len(ALL_MODULES)
    db = pymongodb
    call = db.command("dbstats")
    datasize = call["dataSize"] / 1024
    datasize = str(datasize)
    storage = call["storageSize"] / 1024
    objects = call["objects"]
    collections = call["collections"]
    status = db.command("serverStatus")
    query = status["opcounters"]["query"]
    mongouptime = status["uptime"] / 86400
    mongouptime = str(mongouptime)
    served_chats = len(await get_served_chats())
    served_users = len(await get_served_users())
    total_queries = await get_queries()
    blocked = len(BANNED_USERS)
    sudoers = len(await get_sudoers())
    text = f""" **ʙᴏᴛ's sᴛᴀᴛs ᴀɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ:**

**ɪᴍᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇs:** {mod}
**ᴘʟᴀᴛғᴏʀᴍ:** {sc}
**ʀᴀᴍ:** {ram}
**ᴘʜʏsɪᴄᴀʟ ᴄᴏʀᴇs:** {p_core}
**ᴛᴏᴛᴀʟ ᴄᴏʀᴇs:** {t_core}
**ᴄᴘᴜ ғʀᴇǫᴜᴇɴᴄʏ:** {cpu_freq}

**ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** {pyver.split()[0]}
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** {pyrover}
**ᴘʏ-ᴛɢᴄᴀʟʟs ᴠᴇʀsɪᴏɴ :** {pytgver}

**sᴛᴏʀᴀɢᴇ ᴀᴠᴀɪʟ:** {total[:4]} GiB
**sᴛᴏʀᴀɢᴇ ᴜsᴇᴅ:** {used[:4]} GiB
**sᴛᴏʀᴀɢᴇ ʟᴇғᴛ:** {free[:4]} GiB

**sᴇʀᴠᴇᴅ ᴄʜᴀᴛs:** {served_chats} 
**sᴇʀᴠᴇᴅ ᴜsᴇʀs:** {served_users} 
**ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs:** {blocked} 
**sᴜᴅᴏ ᴜsᴇʀs:** {sudoers} 

**ᴍᴏɴɢᴏ ᴜᴘᴛɪᴍᴇ:** {mongouptime[:4]} Days
**ᴛᴏᴛᴀʟ ᴅʙ sɪᴢᴇ:** {datasize[:6]} Mb
**ᴛᴏᴛᴀʟ ᴅʙ sᴛᴏʀᴀɢᴇ:** {storage} Mb
**ᴛᴏᴛᴀʟ ᴅʙ ᴄᴏʟʟᴇᴄᴛɪᴏɴs:** {collections}
**ᴛᴏᴛᴀʟ ᴅʙ ᴋᴇʏs:** {objects}
**ᴛᴏᴛᴀʟ ᴅʙ ǫᴜᴇʀɪᴇs:** `{query}`
**ᴛᴏᴛᴀʟ ʙᴏᴛ ǫᴜᴇʀɪᴇs:** `{total_queries} `
    """
    med = InputMediaPhoto(media=config.STATS_IMG_URL, caption=text)
    try:
        await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
    except MessageIdInvalid:
        await CallbackQuery.message.reply_photo(photo=config.STATS_IMG_URL, caption=text, reply_markup=upl)

@app.on_callback_query(
    filters.regex(pattern=r"^(TOPMARKUPGET|GETSTATS|GlobalStats)$")
    & ~BANNED_USERS
)
@languageCB
async def back_buttons(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    command = CallbackQuery.matches[0].group(1)
    if command == "TOPMARKUPGET":
        upl = top_ten_stats_markup(_)
        med = InputMediaPhoto(
            media=config.GLOBAL_IMG_URL,
            caption=_["gstats_9"],
        )
        try:
            await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(photo=config.GLOBAL_IMG_URL, caption=_["gstats_9"], reply_markup=upl)
    if command == "GlobalStats":
        upl = get_stats_markup(
            _,
            True if CallbackQuery.from_user.id in SUDOERS else False,
        )
        med = InputMediaPhoto(
            media=config.GLOBAL_IMG_URL,
            caption=_["gstats_10"].format(config.MUSIC_BOT_NAME),
        )
        try:
            await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(photo=config.GLOBAL_IMG_URL, caption=_["gstats_10"].format(config.MUSIC_BOT_NAME), reply_markup=upl)
    if command == "GETSTATS":
        upl = stats_buttons(
            _,
            True if CallbackQuery.from_user.id in SUDOERS else False,
        )
        med = InputMediaPhoto(
            media=config.STATS_IMG_URL,
            caption=_["gstats_11"].format(config.MUSIC_BOT_NAME),
        )
        try:
            await CallbackQuery.edit_message_media(media=med, reply_markup=upl)
        except MessageIdInvalid:
            await CallbackQuery.message.reply_photo(photo=config.STATS_IMG_URL, caption=_["gstats_11"].format(config.MUSIC_BOT_NAME), reply_markup=upl)
