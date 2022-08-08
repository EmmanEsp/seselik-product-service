"""
Configuration test file
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, database_exists

from app.infraestructure.database.common import get_db
from app.infraestructure.database.session import Base
from app.main import app

SQLALCHEMY_DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/tests?sslmode=disable"
)


@pytest.fixture(scope="session")
def db_engine():
    """Creating db engine"""
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
    yield engine


@pytest.fixture(scope="function")
def db(db_engine):
    """Get database session"""
    connection = db_engine.connect()
    connection.begin()

    db = Session(bind=connection)
    app.dependency_overrides[get_db] = lambda: db

    try:
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture(scope="function")
def client(db):
    """API Test Client"""
    app.dependency_overrides[get_db] = lambda: db

    with TestClient(app) as c:
        yield c
