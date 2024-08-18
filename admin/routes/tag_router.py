from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from services.dependencies.services import get_tag_service
from services.schemas import TagCreate
from services.tag_service import TagService

router = APIRouter(prefix='/tag', tags=['tag'])
templates = Jinja2Templates(directory='templates')


@router.get("")
async def get_add_tag(
        request: Request,
):
    return templates.TemplateResponse(
        request=request,
        name='tag.html',
        context={},
    )


@router.get("/all")
async def get_all(
        request: Request,
        tags: TagService = Depends(get_tag_service),
):
    tags = await tags.get_all_tags()
    return templates.TemplateResponse(
        request=request,
        name='tag_all.html',
        context={
            'tags': tags,
        },
    )


@router.post("")
async def add_tag(
        schema: TagCreate,
        tags: TagService = Depends(get_tag_service)
):
    await tags.add_tag(schema=schema)
