from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from services.dependencies.services import get_user_service
from services.schemas import UserCreate, UserTagCreate
from services.user_service import UserService

router = APIRouter(prefix='/user', tags=['user'])
templates = Jinja2Templates(directory='templates')


@router.get("")
async def get_create_user(
        request: Request,
):
    return templates.TemplateResponse(
        request=request,
        name='user.html',
        context={},
    )


@router.get("/all")
async def get_all(
        request: Request,
        users: UserService = Depends(get_user_service)
):
    users = await users.get_all_users()
    return templates.TemplateResponse(
        request=request,
        name='user_all.html',
        context={
            'users': users,
        },
    )


@router.post("")
async def create_user(
        user: UserCreate,
        users: UserService = Depends(get_user_service)
):
    await users.create_user(schema=user)


@router.post("/tag")
async def add_tag(
        schema: UserTagCreate,
        tags: UserService = Depends(get_user_service)
):
    print(schema)
    await tags.add_tag(schema=schema)
