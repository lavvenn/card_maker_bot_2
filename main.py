import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from db.session import Base, engine
from handlers import router

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():

    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await init_db()

    await dp.start_polling(bot)


if __name__ == "__main__":

    asyncio.run(main())
