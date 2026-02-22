from aiogram import Router

from handlers import start, registration


router = Router()

router.include_routers(
    start.router,
    registration.router,
)
