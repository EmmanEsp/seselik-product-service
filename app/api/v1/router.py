"""
Router for V1 version
"""
from fastapi import APIRouter

from app.api.v1.endpoints import healthcheck_endpoints, product_endpoints

v1_router = APIRouter()

v1_router.include_router(
    router=healthcheck_endpoints.router,
    prefix="/healthcheck",
    tags=["Healthcheck"],
)

v1_router.include_router(
    router=product_endpoints.router,
    prefix="/products",
    tags=["Products"],
)
