from newsletter_tag.dependencies.repositories import get_newsletter_tag_repo
from newsletter.dependencies.repositories import get_newsletter_repo
from newsletter.newsletter_service import NewsletterService
from tags.dependencies.repositories import get_tag_repo


def get_newsletter_service() -> NewsletterService:
    return NewsletterService(newsletters=get_newsletter_repo(),
                             tags=get_tag_repo(),
                             newsletter_tags=get_newsletter_tag_repo())
