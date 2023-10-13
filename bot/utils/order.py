import requests

from app.config import settings


def get_orders(telegram_id: str):
    url = f"localhost:8000/api/v1/order/{telegram_id}"
    response = requests.get(url)
    orders = response.json()
    return orders


def add_order(data: dict):
    url = "http://localhost:8000/api/v1/order"
    response = requests.post(url, json=data)
    result = response.json()
    return result


def check_payment(order_id: int):
    url = f"http://localhost:8000/api/v1/order/check-payment/{order_id}"
    response = requests.get(url)
    result = response.json()["status"]
    return result


def change_order_status(order_id: int):
    url = f"http://localhost:8000/api/v1/order/{order_id}"
    response = requests.patch(url)
    return True

