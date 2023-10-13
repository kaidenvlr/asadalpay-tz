import os

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    PG_URL: PostgresDsn = os.getenv("PG_URL")
    ASADAL_TOKEN: str = os.getenv("ASADAL_TOKEN")


settings = Settings()
