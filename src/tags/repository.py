from AbstractRepository import CrudFactory
from tags.models import Tag
from tags.schemas import TagUpdate, TagCreate, TagResponse


class TagRepo(
    CrudFactory(
        Tag,
        TagUpdate,
        TagCreate,
        TagResponse,
    )
):
    pass