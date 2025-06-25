"""Config file for environment variables."""

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = os.getenv("BOT_TOKEN") or ""
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set in environment")
