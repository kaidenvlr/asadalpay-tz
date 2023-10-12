import os

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PG_URL: PostgresDsn = os.getenv("PG_URL")


settings = Settings()
