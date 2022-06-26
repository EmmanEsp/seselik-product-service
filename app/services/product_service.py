"""
Product Services
"""
from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app.infraestructure.database.common import get_session
from app.models.product_model import Product


class ProductService:
    def __init__(self, db: Session = Depends(get_session)):
        """
        Initialize ProductService dependencies
        :param db: get database session
        """
        self.db = db

    def get_all_products(self) -> List[Product]:
        """Get all Products from database"""

        products: List[Product] = self.db.query(Product).all()
        return products
