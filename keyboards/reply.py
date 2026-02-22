from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить данные"),
        ],
    ],
    resize_keyboard=True,
)
