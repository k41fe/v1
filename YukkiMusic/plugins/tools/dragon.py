from YukkiMusic.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck
from YukkiMusic.utils.database import is_muted, mute_on
from YukkiMusic.utils.database import is_muted, mute_off
from YukkiMusic.utils.database import is_music_playing, music_on
from datetime import datetime
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language
import random
import config
import re
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False


@app.on_message(
    command(["ايدي","الايدي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""- Your Name {message.from_user.mention}\n\n- user name @{message.from_user.username}\n\n- hands {message.from_user.id}\n\n- Group Id {message.chat.id}""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝖲𝗈𝗎𝗋𝖼𝖾", url=f"https://t.me/ei222"),
                ],
            ]
        ),
    )
    
@app.on_message(
    command(["نيلوفر","نيلو"])
    & filters.group
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)

@app.on_message(
    command(["نيلوفر"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""ها يحيلي تيكساس 🤍 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝖲𝗈𝗎𝗋𝖼𝖾", url=f"https://t.me/ei222"),
                ],
            ]
        ),
    )             
    
@app.on_message(
     command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b461d00fc4b9fffe7f525.jpg",
        caption=f"""𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 𝖡𝗈𝖳""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋", url=f"https://t.me/G5IID"),
                ],[
                InlineKeyboardButton(
                        "𝖲𝗈𝗎𝗋𝖼𝖾", url=f"https://t.me/L6L6P"),
                ]
            ]
        ),
    )

@app.on_message(
    command(["سورس","السورس"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f50833c6b43b4bd60a1f5.jpg",
        caption=f"""[
𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 𝖭𝖾𝗅𝗈𝗏𝖾𝗋 𝖲𝗈𝗎𝗋𝖼𝖾](https://t.me/ei222)""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                        "𝖯𝗋𝗈𝗀𝗋𝖺𝗆𝗆𝖾𝗋", url=f"https://t.me/L6L6P"),
            ],[
                InlineKeyboardButton("𝖠𝖽𝖽 𝖬𝖾 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 ❤️‍🔥 .", url=f"https://t.me/QYWBOT?startgroup=true"),
            ]
        ]
         ),
     )
    
@app.on_message(
     command(["مبرمج السورس" ,"مطور السورس","المبرمج"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b461d00fc4b9fffe7f525.jpg",
        caption=f"""𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 𝖯𝗋𝗈𝗀𝗋𝖺𝗆𝗆𝖾𝗋 𝖡𝗈𝖳""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton("𝖯𝗋𝗈𝗀𝗋𝖺𝗆𝗆𝖾𝗋", url=f"https://t.me/G5IID"),
                ],[
                InlineKeyboardButton(
                        "𝖲𝗈𝗎𝗋𝖼𝖾", url=f"https://t.me/L6L6P"),
                ]
            ]
        ),
    )
