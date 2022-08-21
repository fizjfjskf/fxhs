## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuzMNFDvNVIoW1dyN2thtreuB5Jki2G85lOkQHfYzW3fh3i5v22ngOIs49KDoGX1aEOn6IRXRe-EvsFUnET-io2Xy07n0klll-Bayo-SMabwOR2HVtRPfLF-jB-27vY0bD8VGNc6p2KItaABZRoNkJvk0V5aMLP3vRmsQpu9pTaHMmgfKgAImIU87PskQG2bf2h_Fj5Ns-lw2fROpvn0iI8GPNN_hTCo4L3RO0EpvhAbrlOsaqeybqvG9hJ1VtQBWS_7GFtHezTfZHPrMNfnS6uZorlsZPL579sivoTz2enqq6k_DmEQ0w4sC1hXtK22kd-J2WKRTtX4PV0nZbdHW7G0=")
BOT_TOKEN = getenv("BOT_TOKEN", "5425525201:AAEHU0RvyTX_NiIQB8xiU8uYk7wXwy2Xf0M")
BOT_NAME = getenv("BOT_NAME", "REPO")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "firas")
OWNER_USERNAME = getenv("OWNER_USERNAME", "OOQOCC")
ALIVE_NAME = getenv("ALIVE_NAME", "firas")
BOT_USERNAME = getenv("BOT_USERNAME", "fjfgvffbot")
OWNER_ID = getenv("OWNER_ID", "5284259786")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "r9dt_8")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ffdt9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "gsgfr")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5284259786").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
