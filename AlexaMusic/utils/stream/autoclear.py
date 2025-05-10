# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import os

import asyncio
from config import autoclean


async def auto_clean(popped):
    async def _auto_clean(popped_item):
        try:
            rem = popped_item.get("file")
            if rem:
                autoclean.discard(rem)
                if all(keyword not in rem for keyword in ("vid_", "live_", "index_")):
                    try:
                        os.remove(rem)
                    except FileNotFoundError:
                        pass
        except Exception:
            pass

    if isinstance(popped, dict):
        await _auto_clean(popped)
    elif isinstance(popped, list):
        await asyncio.gather(*(_auto_clean(pop) for pop in popped))
    else:
        raise ValueError("Expected popped to be a dict or list.")
