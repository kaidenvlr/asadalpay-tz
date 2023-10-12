from fastapi import APIRouter, Depends, status

from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.order import Order, OrderItem
from app.schemas.order import OrderSchema, OrderResponse, OrderItemSchema

router = APIRouter(prefix="/order")


@router.get("/{order_id}", status_code=status.HTTP_200_OK, response_model=OrderResponse)
async def get_order(order_id: int, db_session: AsyncSession = Depends(get_db)):
    order = await Order.get(order_id=order_id, db_session=db_session)
    return order


@router.post("", status_code=status.HTTP_201_CREATED, response_model=OrderResponse)
async def create_order(payload: OrderSchema, db_session: AsyncSession = Depends(get_db)):
    order_items = payload.order_items
    telegram_id = payload.telegram_id

    order = Order(telegram_id=telegram_id)
    await order.save(db_session=db_session)

    order_item_models = []

    for order_item in order_items:
        order_item.order_id = order.id
        order_item_model = OrderItem(**order_item.model_dump())
        await order_item_model.save(db_session=db_session)
        order_item_models.append(order_item_model)

    order.order_items = order_item_models
    return order
