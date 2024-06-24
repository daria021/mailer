from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class UserTag(Base):
    __tablename__ = "user_tag"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user: Mapped[int] = mapped_column(ForeignKey("user.id"))
    tag: Mapped[int] = mapped_column(ForeignKey("tag.id"))
