from fastapi import APIRouter, Depends
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates

from auth.dependencies.services import get_auth_service
from auth.auth_form import auth_code_form
from auth.auth_service_interface import AuthServiceInterface
from auth.exceptions import WrongCredentialsException
from auth.schemas import Credentials

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)

templates = Jinja2Templates(directory='templates')


@router.get("")
async def get_login_page(
        request: Request,
        destination: str = "/newsletter",
):
    return templates.TemplateResponse(
        request=request,
        name='auth.html',
        context={
            "destination": destination
        },
    )


@router.post("")
async def validate_auth_code_backend(
        credentials: Credentials = Depends(auth_code_form),
        auth_service: AuthServiceInterface = Depends(get_auth_service),
) -> JSONResponse:
    try:
        tokens = await auth_service.create_tokens(credentials)
        response = JSONResponse(content={"status": "ok"}, status_code=200)
        response.set_cookie(key="access_token", value=tokens.access_token)
        return response
    except WrongCredentialsException:
        return JSONResponse(content={"status": "error", "message": "Wrong credentials"}, status_code=400)
