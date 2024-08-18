from Repo.AbstractRepository import AbstractSQLAlchemyRepository

from user_tag.models import UserTag
from user_tag.schemas import UserTagResponse, UserTagCreate, UserTagUpdate


class UserTagRepo(
    AbstractSQLAlchemyRepository[
        UserTag,
        UserTagResponse,
        UserTagCreate,
        UserTagUpdate,
    ]
):
    def entity_to_model(self, entity: UserTag) -> UserTagResponse:
        return UserTagResponse(
            id=entity.id,
            user=entity.user,
            tag=entity.tag,
        )

    def model_to_entity(self, model: UserTagResponse) -> UserTag:
        return UserTag(
            user=model.user,
            tag=model.tag,
        )
