from pydantic import BaseSettings

class Settings(BaseSettings):
    bot_token: str
    db_dsn: str

settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
