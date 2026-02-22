from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards import reply

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer("wellcome", reply_markup=reply.main_kb)
