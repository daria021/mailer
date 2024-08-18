from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.datastructures import URL

from auth.schemas import Tokens

from auth.dependencies.services import get_auth_service


async def check_for_auth(
        request: Request,
        call_next,
):
    if request.url.path == "/auth" or request.url.path.startswith("/static"):
        response = await call_next(request)
        return response

    tokens = Tokens(
        access_token=request.cookies.get("access_token", ""),
    )

    auth_service = await get_auth_service()
    lol = await auth_service.check_tokens(tokens)
    is_valid = lol['is_valid']
    if not is_valid:
        destination_url = request.url.path
        url = URL("/auth").include_query_params(destination=destination_url)
        return RedirectResponse(url=url, status_code=303)
    else:
        user_id = lol['user_id']
        request.state.user_id = user_id
        response = await call_next(request)
        return response