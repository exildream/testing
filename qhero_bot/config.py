from pydantic import BaseSettings

class Settings(BaseSettings):
    bot_token: str
    db_dsn: str

settings = Settings()
