from db.database import get_async_session, async_session_maker
from tags.repository import TagRepo


def get_tag_repo() -> TagRepo:
    return TagRepo(session_maker=async_session_maker)
