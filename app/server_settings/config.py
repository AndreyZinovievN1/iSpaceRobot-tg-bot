"""Settings of the stand-alone server node (values come from the environment)."""
import logging
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN", "")
API_KEY = os.getenv("API_KEY")
OWNER_ID = int(os.getenv("OWNER_ID", "0") or 0)

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "5432") or 5432)

# Runtime objects (bot, scheduler) are created by the entry point.
bot = None
scheduler = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
