from tags.dependencies.repositories import get_tag_repo
from user.dependencies.repositories import get_user_repo
from user.user_service import UserService
from user_tag.dependencies.repositories import get_user_tag_repo


def get_user_service() -> UserService:
    return UserService(users=get_user_repo(),
                       user_tags=get_user_tag_repo(),
                       tags=get_tag_repo())
