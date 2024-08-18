from fastapi import APIRouter, Depends

from .dependencies.services import get_newsletter_service
from .schemas import NewsletterCreate, NewsletterResponse, NewsletterUpdate

router = APIRouter(
    prefix="/newsletter",
    tags=["newsletter/"],
)


@router.post("")
async def create_newsletter(newsletter: NewsletterCreate,
                            newsletter_service=Depends(get_newsletter_service)) -> NewsletterResponse:
    newsletter = await newsletter_service.create_newsletter(newsletter=newsletter)
    print(newsletter)
    print("ASDFGHJKL<MNBVCXSDFGHJMNBVCFGHBVGHBVFGHJKJHGASDFGHJHGF")
    return newsletter


@router.get("/{newsletter_id}")
async def get_one_newsletter(newsletter_id: int,
                             newsletter_service=Depends(get_newsletter_service)) -> NewsletterResponse:
    res = await newsletter_service.get_one_newsletter(newsletter_id=newsletter_id)
    return res


@router.get("")
async def get_all_newsletter(
        newsletter_service = Depends(get_newsletter_service)
) -> list[NewsletterResponse]:
    res = await newsletter_service.get_all_newsletter()
    return res


@router.put("/{newsletter_id}")
async def update_newsletter(newsletter_id: int,
                            update: NewsletterUpdate,
                            newsletter_service=Depends(get_newsletter_service)) -> NewsletterResponse:
    user = await newsletter_service.update_newsletter(newsletter_id=newsletter_id, update=update)
    return user


@router.delete("/{newsletter_id}")
async def delete_newsletter(newsletter_id: int,
                            newsletter_service=Depends(get_newsletter_service)) -> None:
    await newsletter_service.delete_newsletter(newsletter_id=newsletter_id)
