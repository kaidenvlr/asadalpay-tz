from aiogram.filters.callback_data import CallbackData


class EnterQuantityItemFactory(CallbackData, prefix="item_quantity"):
    quantity: int


class StageFactory(CallbackData, prefix="stage"):
    stage: str


class ItemChosenFactory(CallbackData, prefix="item_choose"):
    id: int
    title: str
