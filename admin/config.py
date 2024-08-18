from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthSettings(BaseSettings):
    secret_key: SecretStr
    access_token_lifetime_seconds: int = 60 * 60

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')


settings = AuthSettings()
