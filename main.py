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

# --- 🟢 Flask Keep Alive Code (সংশোধিত নাম: web_server) ---
from flask import Flask
from threading import Thread

web_server = Flask('') # Flask-এর নাম পরিবর্তন করে web_server রাখা হলো

@web_server.route('/')
def home():
    return "Bot is alive!"

def run():
    # Render-এর জন্য সঠিক পোর্ট কনফিগারেশন
    port = int(os.environ.get("PORT", 8080))
    web_server.run(host='0.0.0.0', port=port)

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

# 🧠 Bot Modules
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

# -------------------------------------------------------------------------
# আপনার বোটের বাকি সব কমান্ড এবং ফাংশনগুলো এখানে থাকবে
# (যেমন: @app.on_message ইত্যাদি)
# -------------------------------------------------------------------------

# 🚀 Bot Start [সংশোধিত এবং চূড়ান্ত অংশ]
if __name__ == "__main__":
    print("Starting Keep Alive Web Server...")
    keep_alive() # Flask ওয়েব সার্ভার চালু করবে
    
    print("Starting Pyrogram Bot...")
    # এখানে 'app' হলো আপনার Pyrogram Client-এর অবজেক্ট
    # এটি বোটকে সচল রাখবে
    app.run() #
