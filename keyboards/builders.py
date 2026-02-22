from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

groups = ["group1", "group2"]


def goroup_kb_builder() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for group in groups:
        builder.row(InlineKeyboardButton(text=group, callback_data=group), width=2)

    return builder.as_markup()
