from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration for the application.

    Values are loaded from the `.env` file or environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ==========================
    # Application
    # ==========================

    APP_NAME: str = Field(default="QAP")
    APP_VERSION: str = Field(default="1.0.0")
    ENVIRONMENT: str = Field(default="development")
    DEBUG: bool = Field(default=True)

    HOST: str = Field(default="127.0.0.1")
    PORT: int = Field(default=8000)

    # ==========================
    # Database
    # ==========================

    DATABASE_URL: str

    # ==========================
    # JWT
    # ==========================

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ==========================
    # Logging
    # ==========================

    LOG_LEVEL: str = "INFO"

    # ==========================
    # LLM
    # ==========================

    LLM_PROVIDER: str = "openai"
    LLM_MODEL: str = ""
    LLM_API_KEY: str = ""

    # ==========================
    # Cache
    # ==========================

    REDIS_URL: str = ""

    # ==========================
    # Plugins
    # ==========================

    PLUGIN_DIRECTORY: str = "plugins/implementations"


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached Settings object.
    """
    return Settings()


settings = get_settings()