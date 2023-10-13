from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton, ReplyKeyboardMarkup


def get_basic_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Показать товары")],
        [KeyboardButton(text="Корзина")],
        [KeyboardButton(text="История заказов")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_cancel_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Отменить")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


def get_check_order_status_keyboard() -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text="Проверить оплату")]
    ]
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
