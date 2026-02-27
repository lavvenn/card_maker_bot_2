from typing import List

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .session import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int]
    lastname: Mapped[str] = mapped_column(String(100))
    firstname: Mapped[str] = mapped_column(String(100))
    group: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    photo_file_id: Mapped[str] = mapped_column(String(255))


class Curator(Base):

    __tablename__ = "curators"

    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(100))
    firstname: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(30))
    group: Mapped[List["Group"]] = relationship()


class Group(Base):

    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    curator: Mapped[int] = mapped_column(ForeignKey("curators.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(100))
    slug: Mapped[str] = mapped_column(String(100))
