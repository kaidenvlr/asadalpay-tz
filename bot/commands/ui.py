from aiogram import Bot
from aiogram.types import BotCommandScopeAllPrivateChats, BotCommand


async def set_ui_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Начать заново"),
        BotCommand(command="stop", description="Остановить бота"),
    ]

    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeAllPrivateChats(),
    )
