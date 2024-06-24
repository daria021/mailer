from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class UserNewsletter(Base):
    __tablename__ = "user_newsletter"

    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    user: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    newsletter: Mapped[int] = mapped_column(Integer, ForeignKey("newsletter.id"))
