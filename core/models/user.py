from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from core.models import Post


class User(Base):
    username: Mapped[str] = mapped_column(String(25), unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
