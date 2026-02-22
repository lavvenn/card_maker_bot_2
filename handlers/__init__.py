from aiogram import Router

import handlers.start


router = Router()

router.include_routers(
    handlers.start.router,
)
