from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .user import User


class Profile(Base):
    username: Mapped[str] = mapped_column(String(25), unique=True)

    user_id: Mapped["User"] = relationship(back_populates="user")
