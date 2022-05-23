from fastapi import APIRouter, status

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
def get_health_status():
    """
    Get the healthcheck of the app
    """
    return "working with version 0.1.0"
