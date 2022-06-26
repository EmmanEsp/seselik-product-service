"""
Main API entry file
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import v1_router


def init() -> FastAPI:
    """
    Initialize the app.
    - Configure API
    """
    _app = FastAPI(
        title="product-service",
        description="Seselik service to handle products",
        version="0.1.0",
    )
    _app.include_router(router=v1_router, prefix="/api/v1")
    return _app


app = init()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
