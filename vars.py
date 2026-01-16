import os

# 🛰️ API Configuration
API_ID = int(os.environ.get("API_ID", 24670806))
API_HASH = os.environ.get("API_HASH", "82134723a32b2cae76b9cfb3b1570745")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8479840767:AAGU9pgJvC1iTQKXOKeMBPuuQgnLmoqRi9I")

# 🍃 MongoDB Configuration (আপনার দেওয়া URL সরাসরি এখানে বসানো হয়েছে)
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Admin:Golu1234@cluster0.bcz3n2q.mongodb.net/?appName=Cluster0")
MONGO_URL = DATABASE_URL

# 👑 Owner and Admin Configuration
OWNER_ID = int(os.environ.get("OWNER_ID", 8229228616))
# অ্যাডমিন লিস্টে আপনার আইডি ডিফল্ট হিসেবে থাকবে
ADMINS = [int(x) for x in os.environ.get("ADMINS", str(OWNER_ID)).split()]

# 🏷️ Bot Branding
BOT_USERNAME = "@MyMyMyMyisnothingbhaibot"
CREDIT = "MyPrivateBot"

# 💬 Message Formats
AUTH_MESSAGES = {
    "subscription_active": "<b>✅ Subscription Activated!</b>",
    "subscription_expired": "<b>⚠️ Your Subscription Has Ended!</b>",
    "access_denied": "<b>❌ Access Denied!</b>"
}
