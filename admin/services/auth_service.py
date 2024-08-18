from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

import jwt

from auth.auth_service_interface import AuthServiceInterface
from auth.exceptions import WrongCredentialsException
from config import AuthSettings
from services.schemas import UserFilter
from services.user_service import UserService
from auth.schemas import Credentials, Tokens


@dataclass
class AuthService(AuthServiceInterface):
    auth_settings: AuthSettings
    user_service: UserService

    def get_access_token_lifetime_seconds(self) -> int:
        return self.auth_settings.access_token_lifetime_seconds

    async def check_credentials(self, credentials: Credentials,
                                ) -> tuple[bool, str | None]:
        schema = UserFilter(
            email=credentials.email,
            hash_password=credentials.hash_password
        )
        user = await self.user_service.get_filtered_user(schema)
        if user:
            return (True, user.id)

        return (False, None)

    def _generate_tokens(self, user_id: str) -> Tokens:
        now = datetime.now(tz=timezone.utc)
        access_expires = now + timedelta(seconds=self.auth_settings.access_token_lifetime_seconds)
        access_token = jwt.encode(
            payload={
                'exp': access_expires,
                'user_id': user_id,
            },
            key=self.auth_settings.secret_key.get_secret_value(),
            algorithm='HS256'
        )

        return Tokens(
            access_token=access_token,
        )

    async def create_tokens(self, credentials: Credentials) -> Tokens:
        check = await self.check_credentials(credentials)
        if check[0]:
            return self._generate_tokens(user_id=str(check[1]))
        else:
            print("wrong creds")
            raise WrongCredentialsException()

    async def check_tokens(self, tokens: Tokens) -> dict:
        try:
            # Декодируем JWT токен
            decoded_token = jwt.decode(
                jwt=tokens.access_token,
                key=self.auth_settings.secret_key.get_secret_value(),
                algorithms=['HS256']
            )
            # Извлекаем user_id из декодированного токена
            user_id = decoded_token.get('user_id')

            return {
                "is_valid": True,
                "user_id": user_id
            }

        except jwt.ExpiredSignatureError:
            print("Access token expired")
        except Exception as e:
            print(f"An error occurred: {e}")

        return {
            "is_valid": False,
            "user_id": None
        }
