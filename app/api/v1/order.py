from fastapi import APIRouter, Depends, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.exceptions import NonProcessableEntityException, BadRequestException
from app.models.order import Order, OrderItem
from app.schemas.order import OrderSchema, OrderResponse, OrderNativeResponse, CheckPaymentResponse
from app.utils import pay_order, check_payment

router = APIRouter(prefix="/order")


@router.get("/{order_id}", status_code=status.HTTP_200_OK, response_model=OrderNativeResponse)
async def get_order(order_id: int, db_session: AsyncSession = Depends(get_db)):
    order = await Order.get(order_id=order_id, db_session=db_session)
    return order


@router.post("", status_code=status.HTTP_201_CREATED, response_model=OrderResponse)
async def create_order(payload: OrderSchema, db_session: AsyncSession = Depends(get_db)):
    order_items = payload.order_items
    telegram_id = payload.telegram_id

    order = Order(telegram_id=telegram_id, status=False)
    try:
        db_session.add(order)
        await db_session.commit()
    except SQLAlchemyError as ex:
        raise NonProcessableEntityException(msg=repr(ex))

    for order_item in order_items:
        # full_value += order_item.quantity * (await Item.get(db_session=db_session, item_id=order_item.item_id)).price
        order_item_model = OrderItem(**order_item.model_dump())
        order_item_model.order_id = order.id
        try:
            db_session.add(order_item_model)
            await db_session.commit()
        except SQLAlchemyError as ex:
            raise NonProcessableEntityException(msg=repr(ex))

    result = (await pay_order(db_session=db_session, order_items=order_items, order=order))
    order.uuid_asadal = result.json()["uuid"]
    await db_session.commit()
    if result.status_code == 201:
        result = result.json()
        response = {
            "id": order.id,
            "full_value": result.get('amount'),
            "url": result.get('checkout_url')
        }
        # OrderResponse.model_validate(order)
        return response
    else:
        raise BadRequestException(msg="Bad Input Values")


@router.patch("/{order_id}", status_code=status.HTTP_202_ACCEPTED, response_model=OrderNativeResponse)
async def change_status(order_id: int, db_session: AsyncSession = Depends(get_db)):
    order = await Order.get(order_id=order_id, db_session=db_session)
    order.status = True
    await db_session.commit()
    return order


@router.get("/all/{telegram_id}", status_code=status.HTTP_200_OK, response_model=list[OrderNativeResponse])
async def get_orders(telegram_id: str, db_session: AsyncSession = Depends(get_db)):
    return await Order.get_all(telegram_id=telegram_id, db_session=db_session)


@router.get('/check-payment/{order_id}', status_code=status.HTTP_200_OK, response_model=CheckPaymentResponse)
async def get_check_payment(order_id: int, db_session: AsyncSession = Depends(get_db)):
    uuid = (await Order.get(order_id=order_id, db_session=db_session)).uuid_asadal
    return {"status": await check_payment(order_uuid=uuid)}
