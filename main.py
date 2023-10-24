import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.filters import Command

from core.settings import settings
from core.utils.commands import set_commands

from core.handlers.basic import get_start, hello, send_all
from core.handlers.callback import inline_callback


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text="Бот Запущен")


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text="Бот Остановлен")


async def main() -> None:
    bot = Bot(token=settings.bots.bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=['start', 'help']))
    dp.message.register(send_all, Command(commands=['sendall',]))
    dp.message.register(hello, F.text == 'Привет')

    dp.callback_query.register(inline_callback, F.data == "test_funk")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
