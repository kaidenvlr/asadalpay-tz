from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from bot.factories import ItemChosenFactory


def get_items_inline_keyboard(items) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in items:
        builder.button(
            text=item["title"],
            callback_data=ItemChosenFactory(id=item["id"], title=item["title"])
        )
    return builder.as_markup()


def add_order_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    btn = InlineKeyboardButton(
        text="Оформить заказ",
        callback_data="order"
    )
    builder.add(btn)
    return builder.as_markup()


def check_payment_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    btn = InlineKeyboardButton(
        text="Проверить статус платежа",
        callback_data="check-payment"
    )
    builder.add(btn)
    return builder.as_markup()
