from textwrap import dedent

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.keyboards.inline import get_items_inline_keyboard
from bot.utils.item import get_items

flags = {"throttling_key": "default"}
router = Router(name="cmds_item")


@router.message(F.text == "Показать товары")
async def show_items(message: Message, state: FSMContext):
    text = "Вот текущие добавленные в систему товары:\n"
    items = get_items()
    for item in items[:-1]:
        text += dedent(f"""\
        <b>ID</b>: {item["id"]}
        <b>Название</b>: {item["title"]}
        <b>Цена</b>: {item["price"]}
        --------------------------------
        """)
    text += dedent(f"""\
    <b>ID</b>: {items[-1]["id"]}
    <b>Название</b>: {items[-1]["title"]}
    <b>Цена</b>: {items[-1]["price"]}
    """)
    await message.answer(text=dedent(text), reply_markup=get_items_inline_keyboard(items))
