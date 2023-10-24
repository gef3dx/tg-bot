from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Inline Кнопка 1",
            callback_data="test_funk"
        ),
        InlineKeyboardButton(
            text="Inline Кнопка 1",
            url="https://ya.ru"
        ),
    ],
    [
        InlineKeyboardButton(
            text="Inline Кнопка 3",
            url="tg://user?id=284675430"
        ),
    ]
])