from textwrap import dedent

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.inline import add_order_keyboard
from bot.utils.item import get_item_title

flags = {"throttling_key": "default"}
router = Router(name="cmds_cart")


@router.message(F.text == 'Корзина')
async def cmd_cart(message: Message, state: FSMContext):
    text = """\
    <b>Текущая корзина</b>
    
    """
    data = await state.get_data()
    # print(data)
    items = data['cart']['order_items']
    items_definition = list(data['items'])

    for item in items[:-1]:
        title = get_item_title(item["item_id"], items_definition)
        text += dedent(f"""\
        Товар: {title}
        Количество: {item["quantity"]}
        ------------------------------
        """)
    try:
        title = get_item_title(items[-1]["item_id"], items_definition)

        text += dedent(f"""\
        Товар: {title}
        Количество: {items[-1]["quantity"]}
        """)

        await message.answer(dedent(text), reply_markup=add_order_keyboard())
    except IndexError:
        await message.answer(dedent("Корзина пуста"))
