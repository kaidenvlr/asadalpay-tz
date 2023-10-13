import asyncio

from aiogram import Bot, Dispatcher

from bot.commands.base import router as base_router
from bot.commands.item import router as item_router
from bot.commands.ui import set_ui_commands
from bot.config import config


async def main():
    print("Bot is starting . . .")
    bot = Bot(config.BOT_TOKEN, parse_mode="HTML")

    dp = Dispatcher()

    dp.include_router(router=base_router)
    dp.include_router(router=item_router)

    await set_ui_commands(bot)

    print("Bot started!")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
