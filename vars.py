import os
from os import getenv

# 🔐 API & Bot Credentials
API_ID = int(getenv("API_ID", "0")) 
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# 🤖 Bot Username (এটি আপনার লগের এরর ফিক্স করবে)
BOT_USERNAME = getenv("BOT_USERNAME", "MyMyMyMyisnothingbhaibot") 

# 🗄️ Database URL
MONGO_URL = getenv("MONGO_URL", "")

# 👤 Admin & Sudo Users
OWNER_ID = int(getenv("OWNER_ID", "123456789")) 

# 📁 Extra Settings
START_PIC = getenv("START_PIC", "https://telegra.ph/file/default.jpg")
