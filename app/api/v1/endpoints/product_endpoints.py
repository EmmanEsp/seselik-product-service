"""
Product endpoints
"""
from fastapi import APIRouter, Depends, status

from app.services.product_service import ProductService

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
def get_all_products(
    service: ProductService = Depends(),
):
    """Get all product from database"""

    return service.get_all_products()
