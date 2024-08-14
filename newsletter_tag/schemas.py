from typing import Optional

from pydantic import BaseModel, ConfigDict


class NewsletterTagUpdate(BaseModel):
    id: int
    newsletter: int
    tag: str
    model_config = ConfigDict(from_attributes=True)


class NewsletterTagCreate(NewsletterTagUpdate):
    id: int
    newsletter: int
    tag: str


class NewsletterTagResponse(NewsletterTagCreate):
    id: int
    newsletter: int
    tag: str


class NewsletterTagFilter(BaseModel):
    id: Optional[int]
    newsletter: Optional[int]
    tag: Optional[str]