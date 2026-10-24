"""Configuration loaded from environment variables."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]

load_dotenv(BASE_DIR / ".env")

BASE_URL = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
TIMEOUT = float(os.getenv("TIMEOUT", "10"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "2"))
API_KEY = os.getenv("API_KEY")
