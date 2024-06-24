from typing import List

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tags.repository import TagRepo
from user.models import User

from AbstractRepository import CrudFactory
from database import get_async_session
from newsletter import Newsletter
from newsletter.schemas import NewsletterUpdate, NewsletterCreate, NewsletterResponse
from user.models import User
from user.repository import UserRepo
from user.schemas import UserFilter, UserResponse
from user_tag.models import UserTag
from user_tag.schemas import UserTagResponse, UserTagCreate, UserTagUpdate, UserTagFilter


class UserTagRepo(
    CrudFactory(
        UserTag,
        UserTagUpdate,
        UserTagCreate,
        UserTagResponse,
    )
):

    @classmethod
    async def get_users_by_tag(cls,
                               tags: list[str],
                               session: AsyncSession,
                               ) -> List[str]:
        tags_id = []
        for tag in tags:
            schemas = await TagRepo.get_filtered_by(session=session, text=tag)  # лист TagResponse
            tag_id = schemas[0].id
            tags_id.append(tag_id)
        users = []
        emails = []
        for tag_id in tags_id:
            schemas = await UserTagRepo.get_filtered_by(session=session, tag=tag_id)
            users.append(schemas[0].user)

        for user in users:
            user = await UserRepo.get(session=session, record_id=user)
            emails.append(user.email)

        # users_tags = await session.execute(select(cls.model).where(cls.model.tag == tag_id))
        # users_tags = users_tags.scalars().all()
        # users = []
        # for user_tag in users_tags:
        #     user = await session.execute(select(User).where(User.id == user_tag.user))
        #     user = user.scalars().one()
        #     users.append(user.email)
        # users_tags = users_tags.scalars().all()
        return emails
