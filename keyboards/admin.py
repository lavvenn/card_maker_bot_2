from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


main_admin_kb = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="создать профиль")],
        [KeyboardButton(text="админ панель")],
    ],
)

panel = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="последние", callback_data="show_all")],
        [InlineKeyboardButton(text="группы", callback_data="show_groups")],
    ],
)


def last_passes_kb(passes) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for p in passes:
        builder.button(
            text=f"{p.name} ({p.created_at:%d.%m})",
            callback_data=f"pass_{p.id}",
        )

    builder.adjust(1)
    return builder.as_markup()
