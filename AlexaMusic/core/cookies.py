# Copyright (c) 2024 @KSKOP69. All rights reserved.
# Use of this source code is governed by a proprietary license.

# Made by @KSKOP69 with ❤️


import os
import aiohttp
import aiofiles
import asyncio

import config
from ..logging import LOGGER


async def fetch_content(session: aiohttp.ClientSession, url: str):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except aiohttp.ClientError as e:
        LOGGER(__name__).error(f"Error fetching from {url}: {e}")
        return ""


async def save_file(content: str, file_path: str):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        async with aiofiles.open(file_path, "w") as file:
            await file.write(content)
        return file_path
    except Exception as e:
        LOGGER(__name__).error(f"Error saving file {file_path}: {e}")
        return ""


async def save_cookies():
    full_url: str = str(config.COOKIES)
    paste_id: str = full_url.split("/")[-1]
    pastebin_url: str = f"https://batbin.me/raw/{paste_id}"

    async with aiohttp.ClientSession() as session:
        content = await fetch_content(session, pastebin_url)

        if content:
            file_path = "cookies/cookies.txt"
            saved_path = await save_file(content, file_path)

            if saved_path and os.path.getsize(saved_path) > 0:
                LOGGER(__name__).info(f"Cookies saved successfully to {saved_path}.")
            else:
                LOGGER(__name__).error("Failed to save cookies or the file is empty.")
        else:
            LOGGER(__name__).error("Failed to fetch cookies.")
