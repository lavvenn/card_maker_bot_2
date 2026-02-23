from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


confirmation_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="✅", callback_data="aprove")],
        [InlineKeyboardButton(text="❌", callback_data="disprove")],
    ],
)
