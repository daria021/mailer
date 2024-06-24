from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from tags.repository import TagRepo
from tags.schemas import TagResponse, TagCreate

router = APIRouter(
    prefix="/tag",
    tags=["tag/"]
)

@router.post("/add", response_model=TagResponse)
async def add_tag(text: str,
                      create: TagCreate,
                      session: AsyncSession = Depends(get_async_session)):
    user = await TagRepo.create(text=text, session=session)
    return user