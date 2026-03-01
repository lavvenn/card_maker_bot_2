from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from db.repository import UserRepository
from db.session import SessionLocal
from keyboards import reply

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    async with SessionLocal() as session:
        repo = UserRepository(session)

        existing_user = await repo.get_by_telegram_id(message.from_user.id)

        if existing_user:
            await message.answer(f"{existing_user.role}", reply_markup=reply.main_kb)
        else:
            await repo.create(
                telegram_id=message.from_user.id,
            )
            await message.answer("wellcome", reply_markup=reply.main_kb)
