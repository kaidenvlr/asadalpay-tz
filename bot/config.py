import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")


config = Config()
