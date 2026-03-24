from aiogram import Router
from aiogram.filters import IS_ADMIN

from . import group

router = Router()

router.include_routers(
    group.router,
)

router.message.filter
