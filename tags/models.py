from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.database import Base


class Tag(Base):
    __tablename__="tag"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    text: Mapped[str]
    newsletters: Mapped[list["Newsletter"]] = relationship('Newsletter', secondary='newsletter_tag', back_populates='tags', lazy='selectin')
    users: Mapped[list["User"]] = relationship('User', secondary='user_tag', back_populates='tags', lazy='selectin')