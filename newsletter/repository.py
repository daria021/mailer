from Repo.AbstractRepository import AbstractSQLAlchemyRepository
from newsletter import Newsletter
from newsletter.schemas import NewsletterUpdate, NewsletterCreate, NewsletterResponse


class NewsletterRepo(
    AbstractSQLAlchemyRepository[
        Newsletter,
        NewsletterResponse,
        NewsletterCreate,
        NewsletterUpdate,
    ]
):
    def entity_to_model(self, entity: Newsletter) -> NewsletterResponse:
        return NewsletterResponse(
            id=entity.id,
            user=entity.user,
            subject=entity.subject,
            text=entity.text,
            tags=entity.tags,
            target_time=entity.target_time,
        )

    def model_to_entity(self, model: NewsletterResponse) -> Newsletter:
        return Newsletter(
            user=model.user,
            subject=model.subject,
            text=model.text,
            target_time=model.target_time
        )
    #
    # async def create(self, **kwargs) -> NewsletterResponse:
    #     news = {
    #         'user': kwargs['user'],
    #         'subject': kwargs['subject'],
    #         'text': kwargs['text'],
    #         'target_time': kwargs['target_time'],
    #     }
    #     instance: Newsletter = self.entity(**news)
    #     async with self.session_maker() as session:
    #         async with session.begin():
    #             session.add(instance)  # Добавляем экземпляр в сессию
    #         await session.commit()  # Коммитим транзакцию после выхода из блока `begin`
    #         await session.refresh(instance)  # Обновляем экземпляр после коммита
    #
    #     tags = kwargs['tags']
    #     tags_repo = get_tag_repo()
    #     for tag in tags:
    #         schema: list[TagResponse] = await tags_repo.get_filtered_by(text=tag)
    #         news_tag = {'newsletter': instance.id, 'tag': schema[0].id}
    #         logging.getLogger(__name__).info(news_tag)
    #
    #         instance_2: NewsletterTag = NewsletterTag(**news_tag)
    #         session.add(instance_2)
    #         await session.commit()
    #
    #     await session.refresh(instance)
    #
    #     res: NewsletterResponse = self.entity_to_model(instance)
    #     return res
