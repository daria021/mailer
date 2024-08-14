from dataclasses import dataclass

from tags.repository import TagRepo
from tags.schemas import TagCreate


@dataclass
class TagService:
    tags: TagRepo

    async def add_tag(self,
                      text: str,
                      ):
        create = TagCreate(text=text)
        user = await self.tags.create(create)
        return user
