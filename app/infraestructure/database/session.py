"""
Session creation file
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.settings.database_settings import get_postgres_uri

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(
        url=get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    ),
)

Base = declarative_base()
