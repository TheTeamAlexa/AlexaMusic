# Copyright (C) 2025 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

"""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2021 ~ Present Team Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""

import config
from typing import Union

from pyrogram.types import InlineKeyboardButton


def setting_markup(_):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_1"], callback_data="AQ"),
            InlineKeyboardButton(text=_["ST_B_2"], callback_data="VQ"),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_3"], callback_data="AU"),
            InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG"),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_5"], callback_data="PM"),
            InlineKeyboardButton(text=_["ST_B_7"], callback_data="CM"),
        ],
        [
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍",
                url=config.SUPPORT_GROUP,
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def audio_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_8"].format("✅") if low == True else _["ST_B_8"].format("")
                ),
                callback_data="LQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_9"].format("✅")
                    if medium == True
                    else _["ST_B_9"].format("")
                ),
                callback_data="MQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_10"].format("✅")
                    if high == True
                    else _["ST_B_10"].format("")
                ),
                callback_data="HQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def video_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_11"].format("✅")
                    if low == True
                    else _["ST_B_11"].format("")
                ),
                callback_data="LQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_12"].format("✅")
                    if medium == True
                    else _["ST_B_12"].format("")
                ),
                callback_data="MQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_13"].format("✅")
                    if high == True
                    else _["ST_B_13"].format("")
                ),
                callback_data="HQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
    sug: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_7"], callback_data="CMANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_14"] if status == True else _["ST_B_15"],
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_26"], callback_data="COMMANDANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_14"] if dels == True else _["ST_B_15"],
                callback_data="COMMANDELMODE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_27"], callback_data="SUGGANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_14"] if sug == True else _["ST_B_15"],
                callback_data="SUGGESTIONCHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def auth_users_markup(_, status: Union[bool, str] = None):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_3"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_16"] if status == True else _["ST_B_17"],
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_18"], callback_data="AUTHLIST"),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_19"], callback_data="SEARCHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_20"] if Direct == True else _["ST_B_21"],
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_22"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_16"] if Group == True else _["ST_B_17"],
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_25"], callback_data="PLAYTYPEANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_16"] if Playtype == True else _["ST_B_17"],
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
