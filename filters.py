from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdminFilter(BaseFilter):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    async def __call__(self, message: Message) -> bool:
        role = await self.user_repository.get_user_role(message.from_user.id)
        return role == "admin"
