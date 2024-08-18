from Repo.AbstractRepository import AbstractSQLAlchemyRepository
from tags.models import Tag
from tags.schemas import TagUpdate, TagCreate, TagResponse


class TagRepo(
    AbstractSQLAlchemyRepository[
        Tag,
        TagResponse,
        TagCreate,
        TagUpdate,
    ]
):
    def entity_to_model(self, entity: Tag) -> TagResponse:
        return TagResponse(
            id=entity.id,
            text=entity.text,
        )

    def model_to_entity(self, model: TagResponse) -> Tag:
        return Tag(
            text=model.text,
        )
