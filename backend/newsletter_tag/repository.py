from Repo.AbstractRepository import AbstractSQLAlchemyRepository
from newsletter_tag.models import NewsletterTag
from newsletter_tag.schemas import NewsletterTagCreate, NewsletterTagResponse, NewsletterTagUpdate



class NewsletterTagRepo(
    AbstractSQLAlchemyRepository[
        NewsletterTag,
        NewsletterTagResponse,
        NewsletterTagCreate,
        NewsletterTagUpdate,
    ]
):
    def entity_to_model(self, entity: NewsletterTag) -> NewsletterTagResponse:
        return NewsletterTagResponse(
            id=entity.id,
            newsletter=entity.newsletter,
            tag=entity.tag,
        )

    def model_to_entity(self, model: NewsletterTagResponse) -> NewsletterTag:
        return NewsletterTag(
            id=model.id,
            newsletter=model.newsletter,
            tag=int(model.tag),
        )
