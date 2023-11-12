from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Привет"
        ),
    ],
    [
        KeyboardButton(
            text="Кнопка 2"
        ),
    ],
    [
        KeyboardButton(
            text="Кнопка 3"
        ),
        KeyboardButton(
            text="Кнопка 4"
        ),
    ],

], resize_keyboard=True, one_time_keyboard=True, input_field_placeholder="Выберите кнопку", selective=True)
