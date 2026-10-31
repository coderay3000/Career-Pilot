from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "CareerPilot AI"
    debug: bool = False

    adzuna_app_id: str
    adzuna_app_key: SecretStr
    adzuna_country: str = "in"


@lru_cache
def get_settings() -> Settings:
    return Settings()