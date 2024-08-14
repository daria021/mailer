from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

from tags.schemas import TagResponse


class NewsletterUpdate(BaseModel):
    text: str
    subject: str
    model_config = ConfigDict(from_attributes=True)
    target_time: Optional[datetime]


class NewsletterCreate(NewsletterUpdate):
    user: int
    subject: str
    text: str
    target_time: Optional[datetime]


class NewsletterResponse(BaseModel):
    id: int
    user: int
    subject: str
    text: str
    tags: Optional[list[TagResponse]]
    target_time: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

