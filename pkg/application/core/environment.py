""" contains the list of environment variables"""
from functools import lru_cache
import os

from pydantic import BaseSettings


@lru_cache()
def get_env_filename():
    """retrieves the environment filename"""
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):  # pylint: disable=too-few-public-methods
    """return a list of environment variables"""

    PROJECT_NAME: str
    PROJECT_VERSION: str

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    DEBUG_MODE: str
    API_VERSION: str
    APP_NAME: str

    class Config:  # pylint: disable=too-few-public-methods
        """config class"""

        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache()
def get_environment_variables():
    """retrieves the values of environment variables"""
    return EnvironmentSettings()
