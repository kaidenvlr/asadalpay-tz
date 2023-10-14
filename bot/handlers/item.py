from contextlib import suppress
from textwrap import dedent

from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from bot.factories import ItemChosenFactory
from bot.keyboards.basic import get_basic_keyboard
from bot.states import CurrentState

router = Router(name="handler_item")


@router.callback_query(ItemChosenFactory.filter(F.id > 0))
async def cb_item_chose(callback: CallbackQuery, callback_data: ItemChosenFactory, state: FSMContext):
    # print("hello")
    item_id = callback_data.id
    item_title = callback_data.title
    print(item_id)
    text = """\
    Напишите количество нужных вам товаров от 1 до 999:
    """
    await state.update_data(item_id=item_id, item_title=item_title)
    with suppress(TelegramBadRequest):
        await callback.message.edit_text(dedent(text))
    await state.set_state(CurrentState.entering_quantity_item)


@router.message(
    CurrentState.entering_quantity_item,
    F.text.regexp(r"\d+")
)
async def enter_quantity_item(message: Message, state: FSMContext):
    quantity = int(message.text)
    if quantity <= 0 or quantity >= 1000:
        await message.answer("Необходимо указать число от 1 до 999")
    else:
        item_data = await state.get_data()
        # print(item_data)
        item_id = item_data.get("item_id", None)
        item_title = item_data.get("item_title", None)
        if item_id is None:
            await message.answer("Произошла ошибка, напишите /stop, а затем /start.")
        items = item_data["items"]
        item_ = {"id": item_id, "title": item_title}
        if item_ not in items:
            items.append(item_)
        cart = item_data.get("cart", {})
        items_in_cart = cart["order_items"]
        flag = False
        for item_in_cart in items_in_cart:
            if item_in_cart["item_id"] == item_id:
                item_in_cart["quantity"] += quantity
                flag = True
            if flag:
                break
        if not flag:
            items_in_cart.append({"item_id": item_id, "quantity": quantity})
        cart = {"telegram_id": str(message.from_user.id), "order_items": items_in_cart}
        await state.update_data(item_id=None, cart=cart, item_title=None, items=items)
        await message.answer("Товар добавлен в корзину!", reply_markup=get_basic_keyboard())
        await state.set_state(None)


@router.message(
    CurrentState.entering_quantity_item,
)
async def incorrect_enter_quantity_item(message: Message):
    text = """\
    Необходимо ввести число, попробуйте еще раз!
    """
    await message.answer(dedent(text))
