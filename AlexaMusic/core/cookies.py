# Copyright (c) 2024 @KSKOP69. All rights reserved.
# Use of this source code is governed by a proprietary license.

# Made by @KSKOP69 with ❤️


import os
import requests
from concurrent.futures import ThreadPoolExecutor

import config
from ..logging import LOGGER


def fetch_content(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        LOGGER(__name__).error(f"Error fetching from {url}: {e}")
        return ""


def save_file(content: str, file_path: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(content)
    return file_path


def save_cookies():
    full_url: str = str(config.COOKIES)
    paste_id: str = full_url.split("/")[-1]
    pastebin_url: str = f"https://batbin.me/raw/{paste_id}"

    with ThreadPoolExecutor() as executor:
        future = executor.submit(fetch_content, pastebin_url)
        content = future.result()

    if content:
        file_path = save_file(content, "cookies/cookies.txt")
        if os.path.getsize(file_path) > 0:
            LOGGER(__name__).info(f"Cookies saved successfully to {file_path}.")
        else:
            LOGGER(__name__).error("Failed to save cookies or the file is empty.")
    else:
        LOGGER(__name__).error("Failed to fetch cookies.")
