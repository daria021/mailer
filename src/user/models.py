from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from tags import Tag


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str]
    hash_password: Mapped[str]
    tags: Mapped[list[Tag]] = relationship('Tag', secondary='user_tag', back_populates='users', lazy='selectin')
