from aiogram import Bot
from aiogram.types import Message

from core.keyboard.reply import reply_keyboard
from core.keyboard.inline import inline_keyboard
from core.database.baseconnect import db
from core.utils.decorators import admin


async def get_start(message: Message, bot: Bot):
    if message.chat.type == "private":
        if not db.user_exists(message.from_user.id):
            db.user_add(message.from_user.id, message.from_user.full_name)
        await message.answer(f"Добро пожаловать {message.from_user.full_name}", reply_markup=reply_keyboard)


@admin
async def send_all(message: Message, bot: Bot):
    if message.chat.type == "private":
        if message.text[9:] != "":
            text = message.text[9:]
            users = db.get_users()
            for row in users:
                await bot.send_message(row[0], text)
            await bot.send_message(message.from_user.id, "Успешная рассылка")
        else:
            await bot.send_message(message.from_user.id, "Вы не отправили текст сообщения!")


async def hello(message: Message, bot: Bot):
    await message.answer(f"Привет {message.from_user.full_name}", reply_markup=inline_keyboard)


@admin
async def add_admin_handler(message: Message, bot: Bot):
    idu = message.text[10:]
    db.add_admin(int(idu))
    if not db.user_exists(idu):
        await message.answer(f"Пользователь с таким id {idu} не подписан", reply_markup=reply_keyboard)
    else:
        await message.answer(f"Пользователь с id {idu} добавлен в список администраторов")


@admin
async def remove_admin_handler(message: Message, bot: Bot):
    idu = message.text[13:]
    db.remove_admin(int(idu))
    if not db.user_exists(idu):
        await message.answer(f"Пользователь с таким id {idu} не подписан", reply_markup=reply_keyboard)
    else:
        await message.answer(f"Пользователь с id {idu} удален из списка администраторов")
