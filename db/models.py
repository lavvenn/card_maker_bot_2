from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .session import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int]
    lastname: Mapped[str] = mapped_column(String(100))
    firstname: Mapped[str] = mapped_column(String(100))
    group: Mapped[str] = mapped_column(String(100))
    photo_file_id: Mapped[str] = mapped_column(String(255))
