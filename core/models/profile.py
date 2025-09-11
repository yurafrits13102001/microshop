from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixins import UserRelationMixin

if TYPE_CHECKING:
    from .user import User


class Profile(UserRelationMixin, Base):
    _user_back_populates = "user"
    _user_id_unique = True
    first_name: Mapped[str | None] = mapped_column(String(55))
    last_name: Mapped[str | None] = mapped_column(String(55))
    bio: Mapped[str | None]
