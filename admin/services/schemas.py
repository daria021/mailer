from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class NewsletterCreate(BaseModel):
    user: Optional[int] = None
    subject: str
    text: str
    target_time: Optional[datetime]


class UserCreate(BaseModel):
    email: str
    hash_password: str


class TagCreate(BaseModel):
    text: str


class TagResponse(TagCreate):
    id: int
    text: str


class UserResponse(BaseModel):
    id: int
    email: str
    hash_password: str
    tags: list[TagResponse]


class UserTagCreate(BaseModel):
    user: int
    tag: str


class UserFilter(BaseModel):
    email: Optional[str] = None
    hash_password: Optional[str] = None


class NewsletterFilter(BaseModel):
    user: Optional[int] = None
    subject: Optional[str] = None
    text: Optional[str] = None
    target_time: Optional[datetime] = None
    tags: Optional[list[TagResponse]] = None
