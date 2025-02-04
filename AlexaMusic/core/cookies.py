# Copyright (c) 2024 @KSKOP69. All rights reserved.
# Use of this source code is governed by a proprietary license.

# Made by @KSKOP69 with ❤️


import os
import requests
from typing import Optional

import config
from ..logging import LOGGER


def save_file(
    pastebin_url: str, file_path: str = "cookies/cookies.txt"
) -> Optional[str]:
    try:
        response = requests.get(pastebin_url)
        response.raise_for_status()

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            file.write(response.text)
        return file_path

    except requests.exceptions.RequestException as e:
        LOGGER(__name__).error(f"Error fetching from {pastebin_url}: {e}")
        return None


def save_cookies() -> None:
    full_url: str = str(config.COOKIES)
    paste_id: str = full_url.split("/")[-1]
    pastebin_url: str = f"https://batbin.me/raw/{paste_id}"

    file_path = save_file(pastebin_url)
    if file_path and os.path.getsize(file_path) > 0:
        LOGGER(__name__).info(f"Cookies saved successfully to {file_path}.")
    else:
        LOGGER(__name__).error("Failed to save cookies or the file is empty.")
