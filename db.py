import os
from datetime import datetime, timedelta
from typing import Optional, Dict, List, Union
from pymongo import MongoClient, errors
from pymongo.database import Database as MongoDatabase
from pymongo.collection import Collection
from vars import *
MONGO_URL = os.environ.get("MONGO_URL")
import colorama
from colorama import Fore, Style
import time
import certifi
from typing_extensions import Literal

# Init colors for Windows
colorama.init()

class Database:
    def __init__(self, max_retries: int = 3, retry_delay: float = 2.0):
        """Initialize MongoDB connection with retry logic"""
        self._print_startup_message()
        self.client: Optional[MongoClient] = None
        self.db: Optional[MongoDatabase] = None
        self.users: Optional[Collection] = None
        self.settings: Optional[Collection] = None
        self._connect_with_retry(max_retries, retry_delay)
        
    def _connect_with_retry(self, max_retries: int, retry_delay: float):
        """Establish MongoDB connection with retry mechanism"""
        for attempt in range(1, max_retries + 1):
            try:
                print(f"{Fore.YELLOW}⌛ Attempt {attempt}/{max_retries}: Connecting to MongoDB...{Style.RESET_ALL}")
                
                self.client = MongoClient(
                    MONGO_URL,
                    serverSelectionTimeoutMS=20000,
                    connectTimeoutMS=20000,
                    socketTimeoutMS=30000,
                    tlsCAFile=certifi.where(),
                    retryWrites=True,
                    retryReads=True
                )
                
                self.client.server_info()
                self.db = self.client.get_database('ITsGOLU_db')
                self.users = self.db['users']
                self.settings = self.db['user_settings']
                
                print(f"{Fore.GREEN}✓ MongoDB Connected Successfully!{Style.RESET_ALL}")
                self._initialize_database()
                return
                
            except Exception as e:
                print(f"{Fore.RED}✕ Connection attempt {attempt} failed: {str(e)}{Style.RESET_ALL}")
                if attempt < max_retries:
                    time.sleep(retry_delay)
                else:
                    raise ConnectionError(f"Failed to connect after {max_retries} attempts")

    def _print_startup_message(self):
        """Print formatted startup message"""
        print(f"\n{Fore.CYAN}{'='*50}")
        print(f"🚀 ITsGOLU_UPLOADER Bot - Database Initialization")
        print(f"{'='*50}{Style.RESET_ALL}\n")

    def _initialize_database(self):
        """Initialize database indexes"""
        try:
            self.users.create_index([("bot_username", 1), ("user_id", 1)], unique=True)
            self.settings.create_index([("user_id", 1)], unique=True)
            print(f"{Fore.GREEN}✓ Database setup complete!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.YELLOW}⚠ Index creation warning: {str(e)}{Style.RESET_ALL}")

    def is_user_authorized(self, user_id: int, bot_username: str = "ITsGOLU_UPLOADER") -> bool:
        """Check user authorization status"""
        if user_id == OWNER_ID or user_id in ADMINS:
            return True
        user = self.users.find_one({"user_id": user_id, "bot_username": bot_username})
        if not user or 'expiry_date' not in user:
            return False
        expiry = user['expiry_date']
        if isinstance(expiry, str):
            expiry = datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S")
        return expiry > datetime.now()

    def add_user(self, user_id: int, name: str, days: int, bot_username: str = "ITsGOLU_UPLOADER"):
        """Add or update a user"""
        expiry_date = datetime.now() + timedelta(days=days)
        self.users.update_one(
            {"user_id": user_id, "bot_username": bot_username},
            {"$set": {"name": name, "expiry_date": expiry_date, "added_date": datetime.now()}},
            upsert=True
        )
        return True, expiry_date

    def list_users(self, bot_username: str = "ITsGOLU_UPLOADER"):
        """List all users for the bot"""
        return list(self.users.find({"bot_username": bot_username}))

    async def cleanup_expired_users(self, bot) -> int:
        """Remove expired users and notify them"""
        current_time = datetime.now()
        expired = self.users.find({"expiry_date": {"$lt": current_time}, "user_id": {"$nin": [OWNER_ID] + ADMINS}})
        count = 0
        for user in expired:
            try:
                await bot.send_message(user["user_id"], "⚠️ Your subscription has expired!")
                self.users.delete_one({"_id": user["_id"]})
                count += 1
            except: continue
        return count

    def get_user_expiry_info(self, user_id: int, bot_username: str = "ITsGOLU_UPLOADER"):
        """Get detailed expiry info for a user"""
        user = self.users.find_one({"user_id": user_id, "bot_username": bot_username})
        if not user or 'expiry_date' not in user: return None
        expiry = user['expiry_date']
        if isinstance(expiry, str): expiry = datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S")
        return {"name": user.get('name'), "expiry_date": expiry.strftime("%d-%m-%Y"), "is_active": expiry > datetime.now()}

    def is_admin(self, user_id: int) -> bool:
        """Check if user is owner or admin"""
        return user_id == OWNER_ID or user_id in ADMINS

    def close(self):
        """Close connection"""
        if self.client:
            self.client.close()

