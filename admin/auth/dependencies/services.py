from services.auth_service import AuthService
from config import settings
from services.dependencies.services import get_user_service


async def get_auth_service() -> AuthService:
    return AuthService(auth_settings=settings, user_service=await get_user_service())
