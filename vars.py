import os
from os import getenv

# 🔐 API & Bot Credentials
# এই মানগুলো Render-এর Environment Variables থেকে আসবে
API_ID = int(getenv("API_ID", "0")) 
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")

# 🗄️ Database URL
MONGO_URL = getenv("MONGO_URL", "")

# 👤 Admin & Sudo Users
# OWNER_ID তে আপনার নিজের টেলিগ্রাম আইডি দিন (ডিফল্ট হিসেবে একটি দেওয়া আছে)
OWNER_ID = int(getenv("OWNER_ID", "123456789")) 

# 📁 Extra Settings
# প্রয়োজনে এখানে আরও ভেরিয়েবল যোগ করতে পারেন
START_PIC = getenv("START_PIC", "https://telegra.ph/file/default.jpg")
LOG_GROUP = int(getenv("LOG_GROUP", "0"))
