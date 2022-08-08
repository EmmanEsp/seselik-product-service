"""
Product Model
"""
from typing import Any
from uuid import uuid4

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID

from app.infraestructure.database.session import Base


class Product(Base):
    """Product Model Class"""

    __tablename__: Any = "product_endpoints"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
