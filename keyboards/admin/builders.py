from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def admission_year_kb(current_year: int):

    builder = InlineKeyboardBuilder()

    for year in range(current_year, current_year - 5, -1):
        builder.row(InlineKeyboardButton(text=year, callback_data=year))

    return builder.as_markup()
