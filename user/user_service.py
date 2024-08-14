from dataclasses import dataclass

from tags.repository import TagRepo
from user import User
from user.repository import UserRepo
from user.schemas import UserUpdate, UserCreate, UserResponse, UserFilter
from user_tag.repository import UserTagRepo
from user_tag.schemas import UserTagCreate


@dataclass
class UserService:
    users: UserRepo
    user_tags: UserTagRepo
    tags: TagRepo

    async def create_user(self,
                          user: UserCreate,
                          ):
        await self.users.create(user)
        user = (await self.users.get_filtered_by(email=user.email))[0]
        print(user)
        return user

    async def add_tag(self,
                      user_id: int,
                      tag: str,
                      ):
        tag = (await self.tags.get_filtered_by(text=tag))[0]
        create_schema = UserTagCreate(
            user=user_id,
            tag=tag.id
        )
        print(create_schema)
        await self.user_tags.create(create_schema)

    async def get_one_user(self,
                           user_id: int,):
        res = await self.users.get(user_id)
        return res

    async def get_all_users(self) -> list[UserResponse]:
        res = await self.users.get_all()
        return res

    async def get_filter_users(self,
                               filters: UserFilter,
                               ) -> UserResponse:
        clean_filters = {key: value for key, value in filters.model_dump().items() if value is not None}
        res = await self.users.get_filtered_by(**clean_filters)
        return res[0]

    async def update_user(self,
                          user_id: int,
                          update: UserUpdate,
                          ):
        user = await self.users.update(obj_id=user_id,  obj=update)
        return user

    async def delete_user(self,
                          user_id: int,
                          ):
        await self.users.delete(obj_id=user_id)
        return
