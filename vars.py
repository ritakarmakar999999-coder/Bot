import os
from os import environ

# API Configuration - Render-এর Environment থেকে আসবে
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# MongoDB Configuration
DATABASE_URL = os.environ.get("DATABASE_URL")
MONGO_URL = DATABASE_URL

# Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", "8229228616"))
# Admins list - Default to owner ID if not provided
ADMINS = [int(x) for x in os.environ.get("ADMINS", str(OWNER_ID)).split()]

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": "<b>✨ Subscription Activated!</b>",
    "subscription_expired": "<b>⚠️ Your Subscription Has Ended</b>",
    "access_denied": "<b>⚠️ Access Denied!</b>"
}
