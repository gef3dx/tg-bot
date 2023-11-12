from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы',
        ),
        BotCommand(
            command='help',
            description='Помощь'
        ),
        BotCommand(
            command='sendall',
            description='Рассылка'
        ),
        BotCommand(
            command='cancel',
            description='Сбросить'
        )
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault(), language_code="ru")