import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_add_order(client: AsyncClient):
    payload = {"title": "Example_add_order", "price": 123.99}
    add_item_response = await client.post("/item", json=payload)
    add_item_id = add_item_response.json()["id"]
    payload = {"telegram_id": "123123123", "order_items": [{"item_id": add_item_id, "quantity": 100}], "status": False}
    response = await client.post("/order", json=payload)

    assert response.status_code == 201
    assert response.json()["full_value"] == 12399.0


@pytest.mark.anyio
async def test_get_order(client: AsyncClient):
    payload = {"title": "Example_get_order", "price": 123.99}
    add_item_response = await client.post("/item", json=payload)
    add_item_id = add_item_response.json()["id"]
    payload = {"telegram_id": "12344321", "order_items": [{"item_id": add_item_id, "quantity": 100}], "status": False}
    response = await client.post("/order", json=payload)

    order_id = response.json()["id"]

    response = await client.get(f"/order/{order_id}")

    assert response.status_code == 200
    assert response.json()["id"] == order_id


@pytest.mark.anyio
async def test_change_status_order(client: AsyncClient):
    payload = {"title": "example_change_status_order", "price": 123.99}
    add_item_response = await client.post("/item", json=payload)
    add_item_id = add_item_response.json()["id"]

    payload = {"telegram_id": "1234321", "order_items": [{"item_id": add_item_id, "quantity": 100}], "status": False}
    response = await client.post("/order", json=payload)
    order_id = response.json()["id"]

    response = await client.patch(f"/order/{order_id}")

    assert response.status_code == 202
    assert response.json()["id"] == order_id
    assert response.json()["status"]
