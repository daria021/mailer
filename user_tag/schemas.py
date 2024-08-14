from typing import Optional

from pydantic import BaseModel, ConfigDict

from user.models import User
from tags.models import Tag


class UserTagUpdate(BaseModel):
    user: int
    tag: int

    model_config = ConfigDict(from_attributes=True)


class UserTagCreate(UserTagUpdate):
    user: int
    tag: int


class UserTagResponse(UserTagCreate):
    id: int
    user: int
    tag: int


class UserTagFilter(BaseModel):
    user: Optional[int]
    tag: Optional[int]