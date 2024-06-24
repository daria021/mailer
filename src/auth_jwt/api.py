from fastapi import FastAPI, Body, Depends
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import session

from database import get_async_session
from user import User
from user.repository import UserRepo
from .auth_handler import sign_jwt
from user.schemas import UserCreate
from user.schemas import UserLogin
from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["auth/"],
)

security = HTTPBearer()

@router.get("/", tags=["root"])
async def read_root(sec: str = Depends(security)) -> dict:
    return {"message": f"Welcome to newsletter! Your token is {sec}"}


@router.post("/user/signup", tags=["user"])
async def create_user(user: UserCreate,
                      session: AsyncSession = Depends(get_async_session)):
    user = await UserRepo.create(session=session, **user.model_dump())
    return sign_jwt(user.email)


def check_user(data: UserLogin):
    filters = {"email": data.email, "hash_password": data.password}
    user = UserRepo.get_filtered_by(session=session, **filters)
    if user:
        return True
    return False


@router.post("/user/login", tags=["user"])
async def user_login(user: UserLogin):
    if check_user(user):
        return sign_jwt(user.email)
    return {
        "error": "Wrong login details!"
    }




def main(authorization: str = Depends(security)):
    return authorization.credentials
