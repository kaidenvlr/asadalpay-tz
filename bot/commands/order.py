from textwrap import dedent

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.utils.order import get_orders

flags = {"throttling_key": "default"}
router = Router(name="cmds_orders")


@router.message(F.text == "История заказов")
async def cmd_order_history(message: Message):
    text = """\
    <b>Ваши заказы:</b>
    
    """
    telegram_id = str(message.from_user.id)
    orders = get_orders(telegram_id=telegram_id)
    for order in orders[:-1]:
        text += dedent(f"""\
        ID заказа: {order["id"]}
        Статус: {"Оплачен" if order["status"] else "Не оплачен"}
        --------------------------------
        """)

    try:
        text += dedent(f"""\
        ID заказа: {orders[-1]["id"]}
        Статус: {"Оплачен" if orders[-1]["status"] else "Не оплачен"}-
        """)
        await message.answer(dedent(text))
    except IndexError:
        await message.answer("Ваша история заказов пуста.")
