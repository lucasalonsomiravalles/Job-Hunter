
from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Job Hunter"
    app_env: Literal["development", "testing", "production"] = "development"
    debug: bool = False

    api_v1_prefix: str = "/api/v1"

    openai_api_key: str | None = None
    openai_model: str | None = None

    database_url: str = (
        "postgresql+psycopg://postgres:postgres@localhost:5432/job_hunter"
    )

    log_level: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()