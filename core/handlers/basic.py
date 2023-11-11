from aiogram import Bot
from aiogram.types import Message

from core.keyboard.reply import reply_keyboard
from core.keyboard.inline import inline_keyboard
from core.database.baseconnect import Database
from core.utils.decorators import admin

db = Database("db.sqlite")


@admin
async def get_start(message: Message, bot: Bot):
    if message.chat.type == "private":
        if not db.user_exists(message.from_user.id):
            db.user_add(message.from_user.id, message.from_user.full_name)
        await message.answer(f"Добропожаловать {message.from_user.full_name}", reply_markup=reply_keyboard)


@admin
async def send_all(message: Message, bot: Bot):
    if message.chat.type == "private":
        text = message.text[9:]
        users = db.get_users()
        for row in users:
            try:
                await bot.send_message(row[0], text)
                if int(row(1) != 1):
                    db.set_active(row[0], 1)
            except:
                db.set_active(row[0], 0)
        await bot.send_message(message.from_user.id, "Успешная рассылка")


async def hello(message: Message, bot: Bot):
    await message.answer(f"Привет {message.from_user.full_name}", reply_markup=inline_keyboard)


@admin
async def add_admin_handler(message: Message, bot: Bot):
    id = message.text[10:]
    db.add_admin(int(id))
    if not db.user_exists(id):
        await message.answer(f"Пользователь с таким id {id} не подписан", reply_markup=reply_keyboard)
    else:
        await message.answer(f"Пользователь с id {id} добавлен в список администраторов")


@admin
async def remove_admin_handler(message: Message, bot: Bot):
    id = message.text[13:]
    db.remove_admin(int(id))
    if not db.user_exists(id):
        await message.answer(f"Пользователь с таким id {id} не подписан", reply_markup=reply_keyboard)
    else:
        await message.answer(f"Пользователь с id {id} удален из списока администраторов")
