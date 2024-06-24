from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class NewsletterTag(Base):
    __tablename__ = "newsletter_tag"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    newsletter: Mapped[int] = mapped_column(ForeignKey("newsletter.id"))
    tag: Mapped[int] = mapped_column(ForeignKey("tag.id"))
