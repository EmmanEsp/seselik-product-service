"""
Database common functions
"""
from typing import Generator

from app.infraestructure.database.session import Session


def get_session() -> Generator:
    """Get database session"""
    db = Session()
    try:
        return db
    finally:
        db.close()
