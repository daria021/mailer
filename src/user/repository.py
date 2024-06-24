from fastapi import Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from AbstractRepository import CrudFactory
from database import get_async_session
from user.schemas import UserUpdate, UserCreate, UserResponse
from user.models import User
from user_tag import UserTag


class UserRepo(
    CrudFactory(
        User,
        UserUpdate,
        UserCreate,
        UserResponse,
    )
):
    pass