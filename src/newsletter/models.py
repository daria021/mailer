from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from nesletter_tag import NewsletterTag
from tags import Tag


class Newsletter(Base):
    __tablename__ = "newsletter"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    subject: Mapped[str]
    text: Mapped[str]
    tags: Mapped[list[Tag]] = relationship('Tag', secondary='newsletter_tag', back_populates='newsletters', lazy='selectin')
    target_time: Mapped[Optional[datetime]]

