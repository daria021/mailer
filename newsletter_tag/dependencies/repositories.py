from db.database import async_session_maker
from newsletter_tag.repository import NewsletterTagRepo


def get_newsletter_tag_repo() -> NewsletterTagRepo:
    return NewsletterTagRepo(session_maker=async_session_maker)


