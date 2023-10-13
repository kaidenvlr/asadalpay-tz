from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.factories import ItemChosenFactory
from bot.utils.item import get_items


def get_items_inline_keyboard(items) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in items:
        builder.button(
            text=item["title"],
            callback_data=ItemChosenFactory(id=item["id"]).pack()
        )
    return builder.as_markup(resize_keyboard=True)
