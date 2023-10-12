import pytest
from httpx import AsyncClient


@pytest.mark.anyio
async def test_add_item(client: AsyncClient):
    payload = {"title": "Example", "price": 123.99}
    response = await client.post("/item", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


@pytest.mark.anyio
async def test_get_item(client: AsyncClient):
    payload = {"title": "Example-2", "price": 123.12}
    response = await client.post("/item", json=payload)
    print(response.json())
    item_id = response.json()["id"]
    response = await client.get(f"/item/{item_id}")
    assert response.status_code == 200
    assert response.json()["id"] == item_id


@pytest.mark.anyio
async def test_update_item(
        client: AsyncClient,
):
    payload = {"title": "Example_Pre_Patch", "price": 123.99}
    patch_payload = {"title": "Example_Post_Patch", "price": 123.12}
    response = await client.post("/item", json=payload)
    item_id = response.json()["id"]
    response = await client.patch(f"/item/{item_id}", json=patch_payload)
    assert response.status_code == 202
    assert response.json()["price"] == patch_payload["price"]


@pytest.mark.anyio
async def test_delete_item(client: AsyncClient):
    payload = {"title": "Example_delete", "price": 123.12}
    response = await client.post("/item", json=payload)
    print(response.json())
    item_id = response.json()["id"]
    response = await client.delete(f"/item/{item_id}")
    assert response.status_code == 200


@pytest.mark.anyio
async def test_get_items(client: AsyncClient):
    response = await client.get("/item")
    assert response.status_code == 200
