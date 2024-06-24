from AbstractRepository import CrudFactory
from nesletter_tag.models import NewsletterTag
from nesletter_tag.schemas import NewsletterTagCreate, NewsletterTagResponse, NewsletterTagUpdate



class NewsletterTagRepo(
    CrudFactory(
        NewsletterTag,
        NewsletterTagUpdate,
        NewsletterTagCreate,
        NewsletterTagResponse,
    )
):
    pass