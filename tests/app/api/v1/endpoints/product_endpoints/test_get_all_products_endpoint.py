"""
Testing Get All Product Endpoint
"""
from fastapi import status
from fastapi.testclient import TestClient


def test_get_all_products(client: TestClient) -> None:
    """Get All Products return 200 OK and Product List"""
    # Act
    raw_response = client.get("/api/v1/products")
    response = raw_response.json()
    # Assert
    assert raw_response.status_code == status.HTTP_200_OK
    assert len(response) == 0
