from fastapi import APIRouter, Depends

from tags.dependencies.services import get_tag_service
from tags.schemas import TagResponse, TagCreate

router = APIRouter(
    prefix="/tag",
    tags=["tag/"]
)


@router.post("", response_model=TagResponse)
async def add_tag(text: str,
                  tag_service=Depends(get_tag_service)):
    user = await tag_service.add_tag(text=text)
    return user
