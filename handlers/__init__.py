from aiogram import Router

from handlers import start, registration, test


router = Router()

router.include_routers(
    start.router,
    registration.router,
    test.router,
)
