from dataclasses import dataclass
from typing import List

from tags.repository import TagRepo
from user.repository import UserRepo
from user_tag.repository import UserTagRepo


@dataclass
class UserTagService:
    user_tags: UserTagRepo
    tags: TagRepo
    users: UserRepo

    async def get_users_by_tag(self,
                               tags: list[str],
                               ) -> List[str]:
        tags_id = []

        for tag in tags:
            schemas = await self.tags.get_filtered_by(text=tag)  # лист TagResponse
            tag_id = schemas[0].id
            tags_id.append(tag_id)
        users_id = []
        emails = []
        for tag_id in tags_id:
            schemas = await self.user_tags.get_filtered_by(tag=tag_id)
            users_id.append(schemas[0].user)

        for user_id in users_id:
            user = await self.users.get(obj_id=user_id)
            emails.append(user.email)

        return emails
