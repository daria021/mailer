from AbstractRepository import CrudFactory

from user_newsletter.models import UserNewsletter
from user_newsletter.schemas import UserNewsletterResponse, UserNewsletterCreate, UserNewsletterUpdate


class UserNewsletterRepo(
    CrudFactory(
        UserNewsletter,
        UserNewsletterUpdate,
        UserNewsletterCreate,
        UserNewsletterResponse,
    )
):
    pass