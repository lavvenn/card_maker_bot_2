from enum import Enum
from typing import List

from sqlalchemy import DateTime, ForeignKey, func, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .session import Base


class UserRole(str, Enum):
    ADMIN = "admin"
    STUDENT = "student"
    CURATOR = "curator"


class PassStatus(str, Enum):
    PRINTED = "printed"
    APROVED = "aproved"
    DISAPROVED = "disaproved"
    VERIFICATION = "verification"


class User(Base):

    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[UserRole] = mapped_column(String(20), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )
    pass_: Mapped["Pass"] = relationship(back_populates="user")


class Pass(Base):

    __tablename__ = "passes"

    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[PassStatus] = mapped_column(
        String(20),
        nullable=False,
        default=PassStatus.VERIFICATION,
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id"))
    user: Mapped["User"] = relationship(back_populates="pass_")
    lastname: Mapped[str] = mapped_column(String(100))
    firstname: Mapped[str] = mapped_column(String(100))
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    photo_file_id: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )


class Group(Base):

    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    curator_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id"))
    passes: Mapped[List["Pass"]] = relationship()
    name: Mapped[str] = mapped_column(String(50))
    slug: Mapped[str] = mapped_column(String(50))
    admission_year: Mapped[DateTime] = mapped_column(DateTime)
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )
