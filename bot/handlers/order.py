from textwrap import dedent

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from bot.keyboards.inline import check_payment_keyboard
from bot.states import CurrentState
from bot.utils.order import add_order, check_payment, change_order_status

router = Router(name="handler_order")


@router.callback_query(F.data == 'order')
async def cb_add_order(callback: CallbackQuery, state: FSMContext):
    data = (await state.get_data())["cart"]
    data = add_order(data)
    await callback.message.edit_text(
        dedent(
            f"""\
            К оплате: {data["full_value"]}
            Для оплаты перейдите на эту ссылку: {data['url']}
            """
        ),
        reply_markup=check_payment_keyboard()
    )
    await state.set_state(CurrentState.check_payment)
    await state.update_data(order_id=data["id"])


@router.callback_query(F.data == 'check-payment', CurrentState.check_payment)
async def cb_check_payment(callback: CallbackQuery, state: FSMContext):
    data = (await state.get_data())["order_id"]
    if check_payment(order_id=data):
        change_order_status(order_id=data)
        await state.set_state(None)
        await callback.message.edit_text("Спасибо за заказ, оплата получена!")
    else:
        await callback.answer(
            text="Оплата не получена, попробуйте оплатить снова!",
            show_alert=True
        )
