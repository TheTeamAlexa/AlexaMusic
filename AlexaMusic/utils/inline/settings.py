# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from typing import Union

from pyrogram.types import InlineKeyboardButton


def setting_markup(_):
    buttons = [
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
                text="• Sᴜᴩᴩᴏʀᴛ •",
                url="https://t.me/Shayri_Music_Lovers",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def audio_quality_markup(
    _,
    LOW: Union[bool, str] = None,
    MEDIUM: Union[bool, str] = None,
    HIGH: Union[bool, str] = None,
    STUDIO: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_8"].format("✅") if LOW == True else _["ST_B_8"].format("")
                ),
                callback_data="LOW",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_9"].format("✅")
                    if MEDIUM == True
                    else _["ST_B_9"].format("")
                ),
                callback_data="MEDIUM",
            ),
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_10"].format("✅")
                    if HIGH == True
                    else _["ST_B_10"].format("")
                ),
                callback_data="HIGH",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_28"].format("✅")
                    if STUDIO == True
                    else _["ST_B_28"].format("")
                ),
                callback_data="STUDIO",
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


def video_quality_markup(
    _,
    SD_360p: Union[bool, str] = None,
    SD_480p: Union[bool, str] = None,
    HD_720p: Union[bool, str] = None,
    FHD_1080p: Union[bool, str] = None,
    QHD_2K: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_29"].format("✅")
                    if SD_360p == True
                    else _["ST_B_29"].format("")
                ),
                callback_data="SD_360p",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_30"].format("✅")
                    if SD_480p == True
                    else _["ST_B_30"].format("")
                ),
                callback_data="SD_480p",
            ),
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_31"].format("✅")
                    if HD_720p == True
                    else _["ST_B_31"].format("")
                ),
                callback_data="HD_720p",
            ),
            InlineKeyboardButton(
                text=(
                    _["ST_B_32"].format("✅")
                    if FHD_1080p == True
                    else _["ST_B_32"].format("")
                ),
                callback_data="FHD_1080p",
            ),
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_33"].format("✅")
                    if QHD_2K == True
                    else _["ST_B_33"].format("")
                ),
                callback_data="QHD_2K",
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


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
    sug: Union[bool, str] = None,
):
    buttons = [
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
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
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
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
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
    return buttons
