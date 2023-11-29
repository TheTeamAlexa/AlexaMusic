import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "乛𝘼𝙇𝙀𝙓𝘼🕊️⃝🦋⁪⁬𝙈𝙐𝙎𝙄𝘾")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6174058850 5745099463").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/TheTeamAlexa/AlexaMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Alexa_BotUpdates")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Alexa_Help")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", None)

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = "https://te.legra.ph/file/e25cde013654032495ee8.jpg"

PING_IMG_URL = "https://te.legra.ph/file/83b244a504e3e0d3d3501.jpg"

PLAYLIST_IMG_URL = "https://te.legra.ph/file/3cf9faa3640786e961104.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/cd9c7fdb783ac9b8c461d.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/37f718acbea41707bdf0c.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        print(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        print(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()
