from enum import Enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .session import Base


class UserRole(str, Enum):
    ADMIN = "admin"
    STUDENT = "student"
    CURATOR = "curator"


class User(Base):

    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[UserRole] = mapped_column(String(20), nullable=False)
    pass_: Mapped["Pass"] = relationship(back_populates="user")


class Pass(Base):

    __tablename__ = "passes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id"))
    user: Mapped["User"] = relationship(back_populates="pass_")
    lastname: Mapped[str] = mapped_column(String(100))
    firstname: Mapped[str] = mapped_column(String(100))
    group: Mapped[str] = mapped_column(String(100))
    photo_file_id: Mapped[str] = mapped_column(String(255))
