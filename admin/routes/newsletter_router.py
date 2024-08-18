from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from services.dependencies.services import get_newsletter_service
from services.newsletter_service import NewsletterService
from services.schemas import NewsletterCreate, NewsletterFilter

router = APIRouter(prefix='/newsletter', tags=['Newsletter'])
templates = Jinja2Templates(directory='templates')


@router.get("/all")
async def get_all(
        request: Request,
        newsletters: NewsletterService = Depends(get_newsletter_service)
):
    newsletters = await newsletters.get_all_newsletter()
    return templates.TemplateResponse(
        request=request,
        name='newsletter_all.html',
        context={
            'newsletters': newsletters,
        },
    )


@router.get("")
async def get_create_newsletter(
        request: Request,
):
    return templates.TemplateResponse(
        request=request,
        name='newsletter.html',
        context={},
    )


@router.post("")
async def create_newsletter(
        request: Request,
        newsletter: NewsletterCreate,
        newsletters: NewsletterService = Depends(get_newsletter_service)
):
    user_id = request.state.user_id

    newsletter.user = user_id
    await newsletters.create_newsletter(schema=newsletter)


@router.get("/user")
async def get_user_newsletter(
        request: Request,
        newsletters: NewsletterService = Depends(get_newsletter_service)
):
    schema = NewsletterFilter(
        user=request.state.user_id
    )
    newsletters = await newsletters.get_filtered_newsletter(schema)
    return templates.TemplateResponse(
        request=request,
        name='user_newsletters.html',
        context={
            'newsletters': newsletters,
        },
    )


@router.delete("/{newsletter_id}")
async def delete_newsletter(
        subject: str,
        newsletters: NewsletterService = Depends(get_newsletter_service)
):
    schema = NewsletterFilter(
        subject=subject
    )
    newsletter = await newsletters.get_filtered_newsletter(schema)
    await newsletters.delete_newsletter(newsletter_id=newsletter.id)


@router.get("/{newsletter_id}")
async def view_newsletter(newsletter_id: int,
                          request: Request,
                          newsletter_service: NewsletterService = Depends(get_newsletter_service)):
    newsletter = await newsletter_service.get_one(newsletter_id)
    return templates.TemplateResponse(request=request, name="newsletter_details.html",
                                      context={"newsletter": newsletter})
