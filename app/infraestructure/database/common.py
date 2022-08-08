"""
Database common functions
"""
from typing import Generator

from app.infraestructure.database.session import SessionLocal


def get_db() -> Generator:
    """Get database session"""
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
