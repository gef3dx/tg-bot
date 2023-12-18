from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
import datetime

from .base import Base


class Users(Base):
    user_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    user_name: Mapped[str] = mapped_column(unique=False, nullable=True)
    reg_date: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    is_admin: Mapped[int] = mapped_column(default=0)
    is_block: Mapped[int] = mapped_column(default=0)

    def __str__(self) -> str:
        return f"<User:{self.id}>"
