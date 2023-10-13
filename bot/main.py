import asyncio

from aiogram import Bot, Dispatcher

from bot.commands.base import router as base_router
from bot.commands.cart import router as cart_router
from bot.commands.item import router as item_router
from bot.commands.order import router as order_router
from bot.commands.ui import set_ui_commands
from bot.config import config
from bot.handlers.item import router as item_handler_router
from bot.handlers.order import router as order_handler_router


async def main():
    print("Bot is starting . . .")
    bot = Bot(config.BOT_TOKEN, parse_mode="HTML")

    dp = Dispatcher()

    dp.include_router(router=base_router)
    dp.include_router(router=item_router)
    dp.include_router(router=cart_router)
    dp.include_router(router=order_router)
    dp.include_router(router=item_handler_router)
    dp.include_router(router=order_handler_router)

    await set_ui_commands(bot)

    print("Bot started!")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
