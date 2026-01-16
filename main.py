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

web_server = Flask('')

@web_server.route('/')
def home():
    return "Bot is alive!"

def run():
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
# ... অন্যান্য ইম্পোর্ট ...

# 🧠 Bot Modules
import auth
import nath as helper
from html_handler import html_handler
from nath import *
from vars import *

# 🤖 Pyrogram Client Setup (এটি আপনার কোডে অবশ্যই থাকতে হবে)
# এখানে vars.py থেকে ভেরিয়েবলগুলো অটোমেটিক আসবে অথবা ম্যানুয়ালি বসান
app = Client(
    "Bot-1",
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN
)

# 🛑 Stop Command (অ্যাডমিনের জন্য)
@app.on_message(filters.command("stop") & filters.user(7110188686))
async def stop_bot(client, message):
    await message.reply_text("**বোটটি সফলভাবে বন্ধ করা হয়েছে।** 🛑")
    os._exit(0)

# 🚀 Bot Start [সংশোধিত এবং চূড়ান্ত অংশ]
if __name__ == "__main__":
    print("Starting Keep Alive Web Server...")
    keep_alive() #
    
    print("Starting Pyrogram Bot...")
    # এখানে 'app.run()' এর শেষে কোনো বাড়তি অক্ষর রাখবেন না
    app.run() 
