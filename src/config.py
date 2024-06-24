from fastapi_mail import ConnectionConfig
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    SECRET: str
    JWT_SECRET: SecretStr
    ACCESS_EXPIRE_DAYS: int
    REFRESH_EXPIRE_DAYS: int
    REDIS_HOST: str
    REDIS_PORT: str
    ALGORITHM: str

    @property
    def db_uri(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def redis_url(self):
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class ConnectionConfigFromEnvFile(ConnectionConfig):
    class Config:
        env_file = 'mail.env'
        env_file_encoding = 'utf-8'


mail_conf = ConnectionConfigFromEnvFile()

config = Settings()
