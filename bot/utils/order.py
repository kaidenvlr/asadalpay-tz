import requests

from app.config import settings


def get_orders(telegram_id: str):
    url = f"localhost:8000/api/v1/order/{telegram_id}"
    response = requests.get(url)
    orders = response.json()
    return orders


def add_order(data: dict):
    url = "localhost:8000/api/v1/order"
    response = requests.post(url, json=data)
    result = response.json()
    return result


def check_status(order_id: str):
    url = f"https://api-dev.asadalpay.com/api/orders/{order_id}"
    response = requests.get(url, headers={"Api-Key": settings.ASADAL_TOKEN})
    result = response.json()
    return result
