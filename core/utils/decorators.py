from aiogram import Bot
from aiogram.types import Message
from core.database.baseconnect import db


def admin(func):
    async def decorator(message: Message, bot: Bot):
        if db.is_admin(message.from_user.id):
            await func(message, bot)
        else:
            await message.reply("У вас нет доступа к этой команде!")

    return decorator
