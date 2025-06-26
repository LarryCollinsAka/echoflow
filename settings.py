from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR / ".env")

from config import AppConfig

settings = AppConfig()

from config import AppConfig

# Instantiate settings.
settings = AppConfig()

