# Copyright (C) 2024 by Alexa_Help @ Github, < https://github.com/TheTeamAlexa >
# Subscribe On YT < Jankari Ki Duniya >. All rights reserved. © Alexa © Yukki.

""""
TheTeamAlexa is a project of Telegram bots with variety of purposes.
Copyright (c) 2024 -present Team=Alexa <https://github.com/TheTeamAlexa>

This program is free software: you can redistribute it and can modify
as you want or you can collabe if you have new ideas.
"""


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["PL_B_1"],
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(text=_["PL_B_8"], callback_data="get_top_playlists"),
        ],
        [
            InlineKeyboardButton(text=_["PL_B_4"], callback_data="PM"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [InlineKeyboardButton(text=_["PL_B_9"], callback_data="SERVERTOP global")],
        [InlineKeyboardButton(text=_["PL_B_10"], callback_data="SERVERTOP chat")],
        [InlineKeyboardButton(text=_["PL_B_11"], callback_data="SERVERTOP user")],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="get_playmarkup"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data="play_playlist a"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data="play_playlist b"),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="home_play"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [InlineKeyboardButton(text=_["PL_B_9"], callback_data="SERVERTOP Global")],
        [InlineKeyboardButton(text=_["PL_B_10"], callback_data="SERVERTOP Group")],
        [InlineKeyboardButton(text=_["PL_B_11"], callback_data="SERVERTOP Personal")],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="get_playmarkup"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["PL_B_7"],
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
