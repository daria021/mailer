import logging
import threading
from dataclasses import dataclass

from asgiref.sync import async_to_sync

from newsletter_tag.repository import NewsletterTagRepo
from newsletter_tag.schemas import NewsletterTagCreate
from tags.repository import TagRepo
from tags.schemas import TagResponse
from . import NewsletterRepo
from .delayed_letter_service import delayed_letter
from .schemas import NewsletterCreate, NewsletterUpdate, NewsletterResponse


@dataclass
class NewsletterService:
    newsletters: NewsletterRepo
    tags: TagRepo
    newsletter_tags: NewsletterTagRepo

    async def create_newsletter(
            self,
            newsletter: NewsletterCreate,
    ):
        await self.newsletters.create(newsletter)
        newsletter = (await self.newsletters.get_filtered_by(user=newsletter.user, subject=newsletter.subject,
                                                             text=newsletter.text))[0]

        threading.Thread(
            target=async_to_sync(delayed_letter),
            args=(newsletter.id,),
            name="create newsletter",
        ).start()
        for thread in threading.enumerate():
            print(f"Active thread: {thread.name}")

        return newsletter

    async def get_one_newsletter(self, newsletter_id: int):
        res = await self.newsletters.get(obj_id=newsletter_id)
        return res

    async def get_all_newsletter(self
                                 ) -> list[NewsletterResponse]:
        res = await self.newsletters.get_all()
        return res

    async def update_newsletter(self,
                                newsletter_id: int,
                                update: NewsletterUpdate):
        user = await self.newsletters.update(obj_id=newsletter_id, obj=update)
        return user

    async def delete_newsletter(self, newsletter_id: int,
                                ):
        await self.newsletters.delete(obj_id=newsletter_id)

    async def create(self, **kwargs) -> NewsletterResponse:
        news = NewsletterCreate(
            user=kwargs['user'],
            subject=kwargs['subject'],
            text=kwargs['text'],
            target_time=kwargs['target_time'],
        )
        await self.newsletters.create(news)
        newsletter = (await self.newsletters.get_filtered_by(user=kwargs['user'], subject=kwargs['subject'],
                                                             text=kwargs['text']))[0]
        tags = kwargs['tags']
        for tag in tags:
            schema: list[TagResponse] = await self.tags.get_filtered_by(text=tag)
            news_tag = NewsletterTagCreate(newsletter=newsletter.id,
                                           tag=schema[0].id)

            logging.getLogger(__name__).info(news_tag)

            await self.newsletter_tags.create(news_tag)

        res: NewsletterResponse = self.newsletters.entity_to_model(newsletter)
        return res
