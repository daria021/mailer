from fastapi import APIRouter, Depends

from tags.dependencies.services import get_tag_service
from tags.schemas import TagResponse, TagCreate
from tags.tag_service import TagService

router = APIRouter(
    prefix="/tag",
    tags=["tag/"]
)


@router.post("", response_model=TagResponse)
async def add_tag(schema: TagCreate,
                  tag_service=Depends(get_tag_service)):
    user = await tag_service.add_tag(text=schema.text)
    return user


@router.get("/all")
async def get_all_tags(
        tag_service: TagService = Depends(get_tag_service)
):
    res = await tag_service.get_all()
    return res
