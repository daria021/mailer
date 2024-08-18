from tags.dependencies.repositories import get_tag_repo
from user.dependencies.repositories import get_user_repo
from user_tag.dependencies.repositories import get_user_tag_repo
from user_tag.user_tag_service import UserTagService


def get_user_tag_service() -> UserTagService:
    return UserTagService(user_tags=get_user_tag_repo(),
                          tags=get_tag_repo(),
                          users=get_user_repo())
