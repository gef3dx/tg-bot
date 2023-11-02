from aiogram import Bot
from aiogram.types import CallbackQuery


async def inline_callback(call: CallbackQuery, bot: Bot):
    await call.message.answer("Функция для ин лайн кнопки")
    await call.answer()
