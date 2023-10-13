from textwrap import dedent

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from bot.keyboards.basic import get_basic_keyboard

# from bot.keyboards

flags = {"throttling_key": "default"}
router = Router(name="cmds_start")


@router.message(Command("start"), flags=flags)
async def cmd_start(message: Message):
    start_text = """\
    Привет! Это фронтовая часть тестового задания Asadal Pay.
    Для того, чтобы выбрать товары нажми на кнопку <b>"Показать товары"</b>
    Для того, чтобы открыть корзину, напиши `/cart`
    Для того, чтобы открыть свои заказы, нажми на кнопку <b>"История заказов"</b>
    """
    await message.answer(text=dedent(start_text), reply_markup=get_basic_keyboard())


@router.message(Command("stop"), flags=flags)
async def cmd_stop(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="Спасибо за использование бота! Чтобы начать заново, напиши /start",
        reply_markup=ReplyKeyboardRemove()
    )
