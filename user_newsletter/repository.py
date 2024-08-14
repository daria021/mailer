from Repo.AbstractRepository import AbstractSQLAlchemyRepository
from user_newsletter.models import UserNewsletter
from user_newsletter.schemas import UserNewsletterResponse, UserNewsletterCreate, UserNewsletterUpdate


class UserNewsletterRepo(
    AbstractSQLAlchemyRepository[
        UserNewsletter,
        UserNewsletterResponse,
        UserNewsletterCreate,
        UserNewsletterUpdate,
    ]
):
    def entity_to_model(self, entity: UserNewsletter) -> UserNewsletterResponse:
        return UserNewsletterResponse(
            id=entity.id,
            user=entity.user,
            newsletter=entity.newsletter,
        )

    def model_to_entity(self, model: UserNewsletterResponse) -> UserNewsletter:
        return UserNewsletter(
            id=model.id,
            user=model.user,
            newsletter=model.newsletter,
        )
