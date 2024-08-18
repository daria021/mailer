from fastapi import APIRouter, Depends

from user.schemas import UserCreate, UserUpdate, UserResponse, UserFilter
from user_tag.schemas import UserTagResponse, UserTagCreate
from .dependencies.services import get_user_service

router = APIRouter(
    prefix="/user",
    tags=["user/"],
)


@router.post("")
async def create_user(user: UserCreate,
                      user_service=Depends(get_user_service)):
    user = await user_service.create_user(user=user)
    return user


@router.post("/tag")
async def add_tag(tag: UserTagCreate,
                  user_service=Depends(get_user_service)) -> None:
    print("ASDFGHJKL<MNBVCXSDFGHJMNBVCFGHBVGHBVFGHJKJHGASDFGHJHGF")
    # print(user_id, tag)
    await user_service.add_tag(create_schema=tag)

@router.get("/all")
async def get_all_users(user_service=Depends(get_user_service)) -> list[UserResponse]:
    res = await user_service.get_all_users()
    return res


@router.get("/{user_id}")
async def get_one_user(user_id: int, user_service=Depends(get_user_service)):
    res = await user_service.get_one_user(user_id=user_id)
    return res


@router.get("")
async def get_filter_users(
        filters: UserFilter = Depends(),
        user_service=Depends(get_user_service)
) -> UserResponse:
    res = await user_service.get_filter_users(filters=filters)
    return res


@router.put("/{user_id}")
async def update_user(user_id: int,
                      update: UserUpdate,
                      user_service=Depends(get_user_service)):
    user = await user_service.update_user(user_id=user_id, update=update)
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: int,
                      user_service=Depends(get_user_service)):
    await user_service.delete_user(user_id=user_id)
