import requests
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models import Item, Order
from app.schemas.order import OrderItemSchema


async def pay_order(db_session: AsyncSession, order_items: list[OrderItemSchema], order: Order):
    body = {
        "products": [
            {
                "name": (await Item.get(db_session=db_session, item_id=order_item.item_id)).title,
                "price": (await Item.get(db_session=db_session, item_id=order_item.item_id)).price,
                "quantity": order_item.quantity
            } for order_item in order_items
        ],
        "currency": "KZT",
        "external_id": f"{order.id}",
        "description": f"Заказ #{order.id}",
        "attempts": 5,
        "mcc": "5533",
        "capture_method": "HOLD",
        "back_url": "https://asadalpay.com",
        "notify_url": "https://asadalpay.com"
    }

    result = requests.post(
        url="https://api-dev.asadalpay.com/api/orders/create-order",
        json=body,
        headers={"Api-Key": settings.ASADAL_TOKEN}
    )

    return result


async def check_payment(order_uuid: str):
    url = f"https://api-dev.asadalpay.com/api/orders/{order_uuid}"
    token = settings.ASADAL_TOKEN
    result = requests.get(
        url=url,
        headers={"Api-Key": token}
    )
    if result.status_code == 200:
        return True if result.json()['status'] == 'PAID' else False
