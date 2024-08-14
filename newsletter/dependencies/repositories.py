from db.database import async_session_maker
from newsletter.repository import NewsletterRepo


def get_newsletter_repo() -> NewsletterRepo:
    return NewsletterRepo(session_maker=async_session_maker)


