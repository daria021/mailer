from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from tags.repository import TagRepo
from user_tag import UserTag
from user_tag.schemas import UserTagResponse
from .repository import UserRepo
from user.models import User
from user.schemas import UserResponse, UserCreate, UserUpdate, UserLogin

router = APIRouter(
    prefix="/user",
    tags=["user/"],
)


@router.post("", response_model=UserResponse)
async def create_user(user: UserCreate,
                      session: AsyncSession = Depends(get_async_session)):
    user = await UserRepo.create(session=session, **user.model_dump())
    return user


@router.get("/one", response_model=UserResponse)
async def get_one_user(user_id: int, session: AsyncSession = Depends(get_async_session)):
    res = await UserRepo.get(record_id=user_id, session=session)
    return res


@router.get("/all", response_model=list[UserResponse])
async def get_all_users(session: AsyncSession = Depends(get_async_session)
                        ) -> list[User]:
    res = await UserRepo.get_all(session=session)
    return res


@router.get("/filter", response_model=list[UserResponse])
async def get_filter_users(filters: UserLogin = Depends(),
                           session: AsyncSession = Depends(get_async_session)
                           ) -> User:
    clean_filters = {key: value for key, value in filters.model_dump().items() if value is not None}
    res = await UserRepo.get_filtered_by(session=session, **clean_filters)
    return res


@router.post("/update", response_model=UserResponse)
async def update_user(user_id: int,
                      update: UserUpdate,
                      session: AsyncSession = Depends(get_async_session)):
    user = await UserRepo.update(record_id=user_id, session=session, **update.model_dump())
    return user


@router.post("/delete", response_model=UserResponse)
async def delete_user(user_id: int,
                      session: AsyncSession = Depends(get_async_session)):
    user = await UserRepo.delete(record_id=user_id, session=session)
    return user


# @router.post("/tag", response_model=UserTagResponse)
# async def add_tag(user_id: int,
#                   tag: str,
#                   session: AsyncSession = Depends(get_async_session)):
#     tag = await session.execute(select(Tag).where(Tag.text == tag))
#     tag = tag.scalars().one()
#
#     user_tag = UserTag()
#     user_tag.user = user_id
#     user_tag.tag = tag.id
#
#     session.add(user_tag)
#     await session.commit()
#     await session.refresh(user_tag)
#     return user_tag

@router.post("/tag", response_model=UserTagResponse)
async def add_tag(user_id: int,
                  tag: str,
                  session: AsyncSession = Depends(get_async_session)):
    tag = await TagRepo.get_filtered_by(session=session, text=tag)
    # tag = await session.execute(select(Tag).where(Tag.text == tag))
    # tag = tag.scalars().one()

    user_tag = UserTag()
    user_tag.user = user_id
    user_tag.tag = tag[0].id

    session.add(user_tag)
    await session.commit()
    await session.refresh(user_tag)
    return user_tag
