from typing import Optional

from pydantic import BaseModel, ConfigDict

from newsletter import Newsletter
from user.models import User


class UserNewsletterUpdate(BaseModel):
    id: int
    user: int
    newsletter: int
    model_config = ConfigDict(from_attributes=True)


class UserNewsletterCreate(UserNewsletterUpdate):
    id: int
    user: int
    newsletter: int


class UserNewsletterResponse(UserNewsletterCreate):
    id: int
    user: int
    newsletter: int


class UserNewsletterFilter(UserNewsletterResponse):
    id: Optional[int]
    user: Optional[int]
    newsletter: Optional[int]