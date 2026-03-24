from aiogram import Router

from handlers import start, registration, admin


router = Router()

router.include_routers(
    start.router,
    registration.router,
    admin.router,
)
