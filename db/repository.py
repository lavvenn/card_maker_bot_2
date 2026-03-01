from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Pass, User, UserRole


class UserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_telegram_id(self, telegram_id: int) -> User | None:
        stmt = select(User).where(User.telegram_id == telegram_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(
        self,
        telegram_id: int,
    ) -> User:
        user = User(
            telegram_id=telegram_id,
            role=UserRole.STUDENT,
        )

        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)

        return user


class PassRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_telegram_id(self, telegram_id: int) -> Pass | None:
        stmt = select(Pass).where(Pass.user_id == telegram_id)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def create(
        self,
        telegram_id: int,
        lastname: str,
        firstname: str,
        group: str,
        photo_file_id: str,
    ):
        pass_ = Pass(
            user_id=telegram_id,
            lastname=lastname,
            firstname=firstname,
            group=group,
            photo_file_id=photo_file_id,
        )

        self.session.add(pass_)
        await self.session.commit()
        await self.session.refresh(pass_)
