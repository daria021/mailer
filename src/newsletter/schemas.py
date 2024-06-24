from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, EmailStr, ConfigDict

from tags.schemas import TagResponse
from user.models import User


class NewsletterUpdate(BaseModel):
    text: str
    subject: str
    tags: list[str]
    model_config = ConfigDict(from_attributes=True)
    target_time: Optional[datetime]


class NewsletterCreate(NewsletterUpdate):
    user: int
    subject: str
    text: str
    tags: list[str]
    target_time: Optional[datetime]


class NewsletterResponse(BaseModel):
    id: int
    user: int
    subject: str
    text: str
    tags: Optional[list[TagResponse]]
    target_time: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

