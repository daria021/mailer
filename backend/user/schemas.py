from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr

from tags.schemas import TagResponse


class UserUpdate(BaseModel):
    email: str
    hash_password: str

    model_config = ConfigDict(from_attributes=True)  # для model_validate


class UserCreate(UserUpdate):
    email: str
    hash_password: str


class UserResponse(BaseModel):
    id: int
    email: str
    hash_password: str
    tags: list[TagResponse]


class UserFilter(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None


class UserLogin(BaseModel):
    email: EmailStr
    password: str
