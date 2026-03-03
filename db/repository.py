from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Group, Pass, User, UserRole


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

    async def update(self, user: User, **kwargs):
        for key, value in kwargs.items():
            setattr(user, key, value)

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
        group: Group,
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

    async def update(self, pass_: Pass, **kwargs):
        for key, value in kwargs.items():
            setattr(pass_, key, value)

        await self.session.commit()
        await self.session.refresh(pass_)
        return pass_


class GroupRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, currator_id: int, name: str, slug: str):

        group = Group(currator_id=currator_id, name=name, slug=slug)

        self.session.add(group)
        await self.session.commit()
        await self.session.refresh(group)
