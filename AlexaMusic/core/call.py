# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


import asyncio
import contextlib
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.errors import FloodWait, ChatAdminRequired
from pyrogram.types import InlineKeyboardMarkup

from pytgcalls import PyTgCalls
from pytgcalls import filters as fl
from ntgcalls import TelegramServerError
from pytgcalls.exceptions import NoActiveGroupCall
from pytgcalls.types import (
    ChatUpdate,
    MediaStream,
    StreamEnded,
    GroupCallConfig,
    GroupCallParticipant,
    UpdatedGroupCallParticipant,
    AudioQuality,
    VideoQuality,
)

import config
from AlexaMusic import LOGGER, YouTube, app
from AlexaMusic.misc import db
from AlexaMusic.utils.database import (
    add_active_chat,
    add_active_video_chat,
    get_assistant,
    get_audio_bitrate,
    get_lang,
    get_loop,
    get_video_bitrate,
    group_assistant,
    is_autoend,
    music_on,
    remove_active_chat,
    remove_active_video_chat,
    set_loop,
)
from AlexaMusic.utils.exceptions import AssistantErr
from AlexaMusic.utils.inline.play import stream_markup, telegram_markup
from AlexaMusic.utils.stream.autoclear import auto_clean
from AlexaMusic.utils.thumbnails import gen_thumb
from strings import get_string

autoend = {}
counter = {}
AUTO_END_TIME = 1


async def _clear_(chat_id):
    if popped := db.pop(chat_id, None):
        await auto_clean(popped)
    db[chat_id] = []
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)
    await set_loop(chat_id, 0)


class Call(PyTgCalls):
    def __init__(self):
        self.userbot1 = Client(
            name="Alexa1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
        )
        self.one = PyTgCalls(
            self.userbot1,
            cache_duration=100,
        )
        self.userbot2 = Client(
            name="Alexa2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
        )
        self.two = PyTgCalls(
            self.userbot2,
            cache_duration=100,
        )
        self.userbot3 = Client(
            name="Alexa3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
        )
        self.three = PyTgCalls(
            self.userbot3,
            cache_duration=100,
        )
        self.userbot4 = Client(
            name="Alexa4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
        )
        self.four = PyTgCalls(
            self.userbot4,
            cache_duration=100,
        )
        self.userbot5 = Client(
            name="Alexa5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
        )
        self.five = PyTgCalls(
            self.userbot5,
            cache_duration=100,
        )

    async def pause_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.pause(chat_id)

    async def resume_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.resume(chat_id)

    async def mute_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.mute(chat_id)

    async def unmute_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        await assistant.unmute(chat_id)

    async def stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        with contextlib.suppress(Exception):
            await _clear_(chat_id)
            await assistant.leave_call(chat_id)

    async def force_stop_stream(self, chat_id: int):
        assistant = await group_assistant(self, chat_id)
        with contextlib.suppress(Exception):
            check = db.get(chat_id)
            check.pop(0)
        await remove_active_video_chat(chat_id)
        await remove_active_chat(chat_id)
        with contextlib.suppress(Exception):
            await assistant.leave_call(chat_id)

    async def skip_stream(
        self,
        chat_id: int,
        link: str,
        video: Union[bool, str] = None,
        image: Union[bool, str] = None,
    ):
        assistant = await group_assistant(self, chat_id)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        ksk = GroupCallConfig(auto_start=False)
        if video:
            stream = MediaStream(
                link,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
            )
        else:
            if image and config.PRIVATE_BOT_MODE == str(True):
                stream = MediaStream(
                    link,
                    image,
                    audio_parameters=audio_stream_quality,
                    video_parameters=video_stream_quality,
                )
            else:
                stream = MediaStream(
                    link,
                    audio_parameters=audio_stream_quality,
                    video_flags=MediaStream.Flags.IGNORE,
                )
        await assistant.play(
            chat_id,
            stream,
            config=ksk,
        )

    async def seek_stream(self, chat_id, file_path, to_seek, duration, mode):
        assistant = await group_assistant(self, chat_id)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        stream = (
            MediaStream(
                file_path,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
                ffmpeg_parameters=f"-ss {to_seek} -to {duration}",
            )
            if mode == "video"
            else MediaStream(
                file_path,
                audio_parameters=audio_stream_quality,
                ffmpeg_parameters=f"-ss {to_seek} -to {duration}",
                video_flags=MediaStream.Flags.IGNORE,
            )
        )
        await assistant.play(chat_id, stream)

    async def stream_call(self, link):
        assistant = await group_assistant(self, config.LOG_GROUP_ID)
        await assistant.play(
            config.LOG_GROUP_ID,
            MediaStream(
                link,
                audio_parameters=AudioQuality.STUDIO,
                video_parameters=VideoQuality.FHD_1080p,
            ),
        )
        await asyncio.sleep(10)
        await assistant.leave_call(config.LOG_GROUP_ID)

    async def join_call(
        self,
        chat_id: int,
        original_chat_id: int,
        link,
        video: Union[bool, str] = None,
        image: Union[bool, str] = None,
    ):
        assistant = await group_assistant(self, chat_id)
        ksk = GroupCallConfig(auto_start=False)
        audio_stream_quality = await get_audio_bitrate(chat_id)
        video_stream_quality = await get_video_bitrate(chat_id)
        if video:
            stream = MediaStream(
                link,
                audio_parameters=audio_stream_quality,
                video_parameters=video_stream_quality,
            )
        else:
            if image and config.PRIVATE_BOT_MODE == str(True):
                stream = MediaStream(
                    link,
                    image,
                    audio_parameters=audio_stream_quality,
                    video_parameters=video_stream_quality,
                )
            else:
                stream = (
                    MediaStream(
                        link,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                    if video
                    else MediaStream(
                        link,
                        audio_parameters=audio_stream_quality,
                        video_flags=MediaStream.Flags.IGNORE,
                    )
                )
        try:
            await assistant.play(chat_id, stream, config=ksk)
        except ChatAdminRequired:
            raise AssistantErr(
                "<b>𝖭𝗈 𝖠𝖼𝗍𝗂𝗏𝖾 𝖵𝗂𝖽𝖾𝗈𝖢𝗁𝖺𝗍 𝖥𝗈𝗎𝗇𝖽 .</b>\n\n𝖳𝗋𝗒 𝖺𝖿𝗍𝖾𝗋 𝗀𝗂𝗏𝗂𝗇𝗀 𝖢𝗁𝖺𝗍 𝖠𝖽𝗆𝗂𝗇 𝗆𝖾."
            )
        except NoActiveGroupCall:
            raise AssistantErr("<b>𝖲𝗍𝖺𝗋𝗍 𝖵𝗂𝖽𝖾𝗈 𝖢𝗁𝖺𝗍.<b>\n\n𝖳𝗁𝖾𝗇 𝖳𝗋𝗒 𝖯𝗅𝖺𝗒𝗂𝗇𝗀 𝖲𝗈𝗇𝗀𝗌.")
        except TelegramServerError:
            raise AssistantErr(
                "<b>𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖲𝖾𝗋𝗏𝖾𝗋 𝖤𝗋𝗋𝗈𝗋</b>\n\n𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖨𝗌 𝖧𝖺𝗏𝗂𝗇𝗀 𝖲𝗈𝗆𝖾 𝖨𝗇𝗍𝖾𝗋𝗇𝖺𝗅 𝖯𝗋𝗈𝖻𝗅𝖾𝗆𝗌 , 𝖯𝗅𝖾𝖺𝗌𝖾 𝖳𝗋𝗒 𝖯𝗅𝖺𝗒𝗂𝗇𝗀 𝖠𝗀𝖺𝗂𝗇 𝖮𝗋 𝖱𝖾𝗌𝗍𝖺𝗋𝗍 𝖳𝗁𝖾 𝖵𝗂𝖽𝖾𝗈𝖢𝗁𝖺𝗍 𝖮𝖿 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉."
            )
        await add_active_chat(chat_id)
        await music_on(chat_id)
        if video:
            await add_active_video_chat(chat_id)
        # if await is_autoend():
        #     counter[chat_id] = {}
        #     users = len(await assistant.get_participants(chat_id))
        #     if users == 1:
        #         autoend[chat_id] = datetime.now() + timedelta(minutes=AUTO_END_TIME)

    async def change_stream(self, client, chat_id):
        check = db.get(chat_id)
        popped = None
        loop = await get_loop(chat_id)
        try:
            if loop == 0:
                popped = check.pop(0)
            else:
                loop = loop - 1
                await set_loop(chat_id, loop)
            if popped and config.AUTO_DOWNLOADS_CLEAR == str(True):
                await auto_clean(popped)
            if not check:
                await _clear_(chat_id)
                return await client.leave_call(chat_id)
        except Exception:
            try:
                await _clear_(chat_id)
                return await client.leave_call(chat_id)
            except Exception:
                return
        else:
            queued = check[0]["file"]
            language = await get_lang(chat_id)
            _ = get_string(language)
            title = (check[0]["title"]).title()
            user = check[0]["by"]
            original_chat_id = check[0]["chat_id"]
            streamtype = check[0]["streamtype"]
            audio_stream_quality = await get_audio_bitrate(chat_id)
            video_stream_quality = await get_video_bitrate(chat_id)
            videoid = check[0]["vidid"]
            userid = check[0].get("user_id")
            check[0]["played"] = 0
            video = str(streamtype) == "video"
            if "live_" in queued:
                n, link = await YouTube.video(videoid, True)
                if n == 0:
                    return await app.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                if video:
                    stream = MediaStream(
                        link,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                else:
                    try:
                        image = await YouTube.thumbnail(videoid, True)
                    except Exception:
                        image = None
                    if image and config.PRIVATE_BOT_MODE == str(True):
                        stream = MediaStream(
                            link,
                            image,
                            audio_parameters=audio_stream_quality,
                            video_parameters=video_stream_quality,
                        )
                    else:
                        stream = MediaStream(
                            link,
                            audio_parameters=audio_stream_quality,
                            video_flags=MediaStream.Flags.IGNORE,
                        )
                try:
                    await client.play(chat_id, stream)
                except Exception:
                    return await app.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                # theme = await check_theme(chat_id)
                img = await gen_thumb(videoid)
                button = telegram_markup(_, chat_id)
                run = await app.send_photo(
                    original_chat_id,
                    photo=img,
                    caption=_["stream_1"].format(
                        title[:27],
                        f"https://t.me/{app.username}?start=info_{videoid}",
                        check[0]["dur"],
                        user,
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            elif "vid_" in queued:
                mystic = await app.send_message(original_chat_id, _["call_10"])
                try:
                    file_path, direct = await YouTube.download(
                        videoid,
                        mystic,
                        videoid=True,
                        video=str(streamtype) == "video",
                    )
                except Exception:
                    return await mystic.edit_text(
                        _["call_9"], disable_web_page_preview=True
                    )
                if video:
                    stream = MediaStream(
                        file_path,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                else:
                    try:
                        image = await YouTube.thumbnail(videoid, True)
                    except:
                        image = None
                    if image and config.PRIVATE_BOT_MODE == str(True):
                        stream = MediaStream(
                            file_path,
                            image,
                            audio_parameters=audio_stream_quality,
                            video_parameters=video_stream_quality,
                        )
                    else:
                        stream = MediaStream(
                            file_path,
                            audio_parameters=audio_stream_quality,
                            video_flags=MediaStream.Flags.IGNORE,
                        )
                try:
                    await client.play(chat_id, stream)
                except Exception:
                    return await app.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                # theme = await check_theme(chat_id)
                img = await gen_thumb(videoid)
                button = stream_markup(_, videoid, chat_id)
                await mystic.delete()
                run = await app.send_photo(
                    original_chat_id,
                    photo=img,
                    caption=_["stream_1"].format(
                        title[:27],
                        f"https://t.me/{app.username}?start=info_{videoid}",
                        check[0]["dur"],
                        user,
                    ),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "stream"
            elif "index_" in queued:
                stream = (
                    MediaStream(
                        videoid,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                    if str(streamtype) == "video"
                    else MediaStream(
                        videoid,
                        audio_parameters=audio_stream_quality,
                        video_flags=MediaStream.Flags.IGNORE,
                    )
                )
                try:
                    await client.play(chat_id, stream)
                except Exception:
                    return await app.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                button = telegram_markup(_, chat_id)
                run = await app.send_photo(
                    original_chat_id,
                    photo=config.STREAM_IMG_URL,
                    caption=_["stream_2"].format(user),
                    reply_markup=InlineKeyboardMarkup(button),
                )
                db[chat_id][0]["mystic"] = run
                db[chat_id][0]["markup"] = "tg"
            else:
                if videoid in ["telegram", "soundcloud"]:
                    image = None
                else:
                    try:
                        image = await YouTube.thumbnail(videoid, True)
                    except:
                        image = None
                if video:
                    stream = MediaStream(
                        queued,
                        audio_parameters=audio_stream_quality,
                        video_parameters=video_stream_quality,
                    )
                else:
                    if image and config.PRIVATE_BOT_MODE == str(True):
                        stream = MediaStream(
                            queued,
                            image,
                            audio_parameters=audio_stream_quality,
                            video_parameters=video_stream_quality,
                        )
                    else:
                        stream = MediaStream(
                            queued,
                            audio_parameters=audio_stream_quality,
                            video_flags=MediaStream.Flags.IGNORE,
                        )
                try:
                    await client.play(chat_id, stream)
                except Exception:
                    return await app.send_message(
                        original_chat_id,
                        text=_["call_9"],
                    )
                if videoid == "telegram":
                    button = telegram_markup(_, chat_id)
                    run = await app.send_photo(
                        original_chat_id,
                        photo=(
                            config.TELEGRAM_AUDIO_URL
                            if str(streamtype) == "audio"
                            else config.TELEGRAM_VIDEO_URL
                        ),
                        caption=_["stream_3"].format(title, check[0]["dur"], user),
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                    db[chat_id][0]["mystic"] = run
                    db[chat_id][0]["markup"] = "tg"
                elif videoid == "soundcloud":
                    button = telegram_markup(_, chat_id)
                    run = await app.send_photo(
                        original_chat_id,
                        photo=config.SOUNCLOUD_IMG_URL,
                        caption=_["stream_3"].format(title, check[0]["dur"], user),
                        reply_markup=InlineKeyboardMarkup(button),
                    )
                    db[chat_id][0]["mystic"] = run
                    db[chat_id][0]["markup"] = "tg"
                else:
                    # theme = await check_theme(chat_id)
                    img = await gen_thumb(videoid)
                    button = stream_markup(_, videoid, chat_id)
                    try:
                        run = await app.send_photo(
                            original_chat_id,
                            photo=img,
                            caption=_["stream_1"].format(
                                title[:27],
                                f"https://t.me/{app.username}?start=info_{videoid}",
                                check[0]["dur"],
                                user,
                            ),
                            reply_markup=InlineKeyboardMarkup(button),
                        )
                    except FloodWait as e:
                        await asyncio.sleep(e.value)
                    db[chat_id][0]["mystic"] = run
                    db[chat_id][0]["markup"] = "stream"

    async def ping(self):
        pings = []
        if config.STRING1:
            pings.append(self.one.ping)
        if config.STRING2:
            pings.append(self.two.ping)
        if config.STRING3:
            pings.append(self.three.ping)
        if config.STRING4:
            pings.append(self.four.ping)
        if config.STRING5:
            pings.append(self.five.ping)
        return str(round(sum(pings) / len(pings), 3))

    async def start(self):
        LOGGER(__name__).info("Starting PyTgCalls Client\n")
        if config.STRING1:
            await self.one.start()
        if config.STRING2:
            await self.two.start()
        if config.STRING3:
            await self.three.start()
        if config.STRING4:
            await self.four.start()
        if config.STRING5:
            await self.five.start()

    async def decorators(self):
        @self.one.on_update(fl.chat_update(ChatUpdate.Status.LEFT_CALL))
        @self.two.on_update(fl.chat_update(ChatUpdate.Status.LEFT_CALL))
        @self.three.on_update(fl.chat_update(ChatUpdate.Status.LEFT_CALL))
        @self.four.on_update(fl.chat_update(ChatUpdate.Status.LEFT_CALL))
        @self.five.on_update(fl.chat_update(ChatUpdate.Status.LEFT_CALL))
        async def stream_services_handler(client, update: ChatUpdate):
            await self.stop_stream(update.chat_id)

        @self.one.on_update(fl.stream_end())
        @self.two.on_update(fl.stream_end())
        @self.three.on_update(fl.stream_end())
        @self.four.on_update(fl.stream_end())
        @self.five.on_update(fl.stream_end())
        async def stream_end_handler1(client, update: StreamEnded):
            if update.stream_type != StreamEnded.Type.AUDIO:
                return
            await self.change_stream(client, update.chat_id)

        # @self.one.on_update(
        #     fl.call_participant(
        #         GroupCallParticipant.Action.JOINED | GroupCallParticipant.Action.LEFT
        #     )
        # )
        # @self.two.on_update(
        #     fl.call_participant(
        #         GroupCallParticipant.Action.JOINED | GroupCallParticipant.Action.LEFT
        #     )
        # )
        # @self.three.on_update(
        #     fl.call_participant(
        #         GroupCallParticipant.Action.JOINED | GroupCallParticipant.Action.LEFT
        #     )
        # )
        # @self.four.on_update(
        #     fl.call_participant(
        #         GroupCallParticipant.Action.JOINED | GroupCallParticipant.Action.LEFT
        #     )
        # )
        # @self.five.on_update(
        #     fl.call_participant(
        #         GroupCallParticipant.Action.JOINED | GroupCallParticipant.Action.LEFT
        #     )
        # )
        # async def participants_change_handler(
        #     client, update: UpdatedGroupCallParticipant
        # ):
        #     participant = update
        #     if participant.action not in (
        #         GroupCallParticipant.Action.JOINED,
        #         GroupCallParticipant.Action.LEFT,
        #     ):
        #         return
        #     chat_id = update.chat_id
        #     users = counter.get(chat_id)
        #     if not users:
        #         try:
        #             got = len(await client.get_participants(chat_id))
        #         except Exception:
        #             return
        #         counter[chat_id] = got
        #         if got == 1:
        #             autoend[chat_id] = datetime.now() + timedelta(minutes=AUTO_END_TIME)
        #             return
        #         autoend[chat_id] = {}
        #     else:
        #         final = (
        #             users + 1
        #             if participant.action == GroupCallParticipant.Action.JOINED
        #             else users - 1
        #         )
        #         counter[chat_id] = final
        #         if final == 1:
        #             autoend[chat_id] = datetime.now() + timedelta(minutes=AUTO_END_TIME)
        #             return
        #         autoend[chat_id] = {}


Alexa = Call()
