import logging

from sqlalchemy.ext.asyncio import AsyncSession

from AbstractRepository import CrudFactory, Schema
from nesletter_tag import NewsletterTag
from newsletter import Newsletter
from newsletter.schemas import NewsletterUpdate, NewsletterCreate, NewsletterResponse
from tags.repository import TagRepo
from tags.schemas import TagResponse


class NewsletterRepo(
    CrudFactory(
        Newsletter,
        NewsletterUpdate,
        NewsletterCreate,
        NewsletterResponse,
    )
):
    @classmethod
    async def create(cls, session: AsyncSession, **kwargs) -> Schema:
        news = {
            'user': kwargs['user'],
            'subject': kwargs['subject'],
            'text': kwargs['text'],
            'target_time': kwargs['target_time'],
        }
        instance: Newsletter = cls.model(**news)
        session.add(instance)
        await session.commit()
        await session.refresh(instance)

        tags = kwargs['tags']
        for tag in tags:
            schema: list[TagResponse] = await TagRepo.get_filtered_by(session=session, text=tag)
            news_tag = {'newsletter': instance.id, 'tag': schema[0].id}
            logging.getLogger(__name__).info(news_tag)

            instance_2: NewsletterTag = NewsletterTag(**news_tag)
            session.add(instance_2)
            await session.commit()

        await session.refresh(instance)

        res: NewsletterResponse = cls.get_schema.model_validate(instance)
        return res
