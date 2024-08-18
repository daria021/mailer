from tags.dependencies.repositories import get_tag_repo
from tags.tag_service import TagService


def get_tag_service() -> TagService:
    return TagService(tags=get_tag_repo())
