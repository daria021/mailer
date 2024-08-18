from services.newsletter_service import NewsletterService
from services.tag_service import TagService
from services.user_service import UserService


async def get_newsletter_service():
    return NewsletterService(host="backend", port=8000)


async def get_user_service():
    return UserService(host="backend", port=8000)


async def get_tag_service():
    return TagService(host="backend", port=8000)
