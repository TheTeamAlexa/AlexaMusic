# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import asyncio
from os import path

from yt_dlp import YoutubeDL

from AlexaMusic.utils.formatters import seconds_to_min


class SoundAPI:
    def __init__(self):
        self.opts = {
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "format": "bestaudio[ext=m4a]/bestaudio/best",
            "retries": 3,
            "nooverwrites": False,
            "continuedl": True,
            "quiet": True,
        }

    async def valid(self, link: str):
        return "soundcloud" in link and "sets" not in link

    async def download(self, url):
        d = YoutubeDL(self.opts)
        try:
            info = await asyncio.to_thread(d.extract_info, url)
        except Exception as e:
            print(f"Error: {e}")
            return False
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
        duration_min = seconds_to_min(info["duration"])
        track_details = {
            "title": info["title"],
            "duration_sec": info["duration"],
            "duration_min": duration_min,
            "uploader": info["uploader"],
            "filepath": xyz,
        }
        return track_details, xyz
