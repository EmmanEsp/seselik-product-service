"""
Database Settings
"""
from functools import lru_cache

from pydantic import BaseSettings


class DatabaseSetting(BaseSettings):
    """Database connection settings"""

    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db_name: str


@lru_cache()
def get_database_settings() -> DatabaseSetting:
    """Get database settings"""
    return DatabaseSetting()


def get_postgres_uri():
    """Get database postgres uri"""
    settings: DatabaseSetting = get_database_settings()
    return (
        f"postgresql://"
        f"{settings.postgres_user}:"
        f"{settings.postgres_password}@"
        f"{settings.postgres_host}:"
        f"{settings.postgres_port}/"
        f"{settings.postgres_db_name}"
    )
