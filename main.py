# 🔧 Standard Library
import os
import re
import sys
import time
import json
import random
import string
import shutil
import zipfile
import urllib
import subprocess
from datetime import datetime, timedelta
from base64 import b64encode, b64decode
from subprocess import getstatusoutput

# 🕒 Timezone
import pytz

# --- 🟢 Flask Keep Alive Code (নতুন যুক্ত করা হয়েছে) ---
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ---------------------------------------------------

# 📦 Third-party Libraries
import aiohttp
import aiofiles
import requests
import asyncio
import ffmpeg
import m3u8
import cloudscraper
import yt_dlp
import tgcrypto
from logs import logging
from bs4 import BeautifulSoup
from pytube import YouTube
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# ⚙️ Pyrogram
from pyrogram import Client, filters, idle
from pyrogram.handlers import MessageHandler
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InputMediaPhoto
)
from pyrogram.errors import (
    FloodWait,
    BadRequest,
    Unauthorized,
    SessionExpired,
    AuthKeyDuplicated,
    AuthKeyUnregistered,
    ChatAdminRequired,
    PeerIdInvalid,
    RPCError
)
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified

# 🧠 Bot Modules (সংশোধিত: itsgolu এর বদলে nath)
import auth
import nath as helper
from html_handler import html_handler
from nath import *

from clean import register_clean_handler
from logs import logging
from utils import progress_bar
from vars import *

# Pyromod fix
import pyromod
from db import db

# 🚀 Bot Start Section
if __name__ == "__main__":
    keep_alive() # Flask সার্ভার চালু হবে যাতে Render বট অফ না করে
    print("🚀 Bot is starting...")
    bot.run() # আপনার বট চালু হবে
