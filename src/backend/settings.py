from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 8000

    class Config:
        env_prefix = 'SERVER_'
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
