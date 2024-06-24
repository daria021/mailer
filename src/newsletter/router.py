from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from . import Newsletter
from .delayed_letter import delayed_letter
from .repository import NewsletterRepo
from .schemas import NewsletterCreate, NewsletterResponse, NewsletterUpdate

router = APIRouter(
    prefix="/newsletter",
    tags=["newsletter/"],
)


@router.post("", response_model=NewsletterResponse)
async def create_newsletter(newsletter: NewsletterCreate,
                            session: AsyncSession = Depends(get_async_session)):
    print(11111111111111)
    newsletter = await NewsletterRepo.create(session=session, **newsletter.model_dump())

    await delayed_letter(session=session, newsletter_id=newsletter.id)
    return newsletter
    # return JSONResponse(status_code=200, content={"message": "email has been sent"})


@router.get("/one", response_model=NewsletterResponse)
async def get_one_newsletter(newsletter_id: int, session: AsyncSession = Depends(get_async_session)):
    res = await NewsletterRepo.get(record_id=newsletter_id, session=session)
    return res


@router.get("/all", response_model=list[NewsletterResponse])
async def get_all_newsletter(session: AsyncSession = Depends(get_async_session)
                             ) -> list[Newsletter]:
    res = await NewsletterRepo.get_all(session=session)
    return res


@router.post("/update", response_model=NewsletterResponse)
async def update_newsletter(newsletter_id: int,
                            update: NewsletterUpdate,
                            session: AsyncSession = Depends(get_async_session)):
    user = await NewsletterRepo.update(record_id=newsletter_id, session=session, **update.model_dump())
    return user


@router.post("/delete", response_model=NewsletterResponse)
async def delete_newsletter(newsletter_id: int,
                            session: AsyncSession = Depends(get_async_session)):
    user = await NewsletterRepo.delete(record_id=newsletter_id, session=session)
    return user
