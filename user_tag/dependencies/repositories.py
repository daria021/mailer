from db.database import async_session_maker
from user_tag.repository import UserTagRepo


def get_user_tag_repo() -> UserTagRepo:
    return UserTagRepo(session_maker=async_session_maker)
