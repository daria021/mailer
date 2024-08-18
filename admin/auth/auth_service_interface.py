from abc import ABC, abstractmethod

from .schemas import Credentials, Tokens


class AuthServiceInterface(ABC):
    @abstractmethod
    def get_access_token_lifetime_seconds(self) -> int:
        ...

    @abstractmethod
    def check_credentials(self, credentials: Credentials) -> bool:
        ...

    @abstractmethod
    async def create_tokens(self, credentials: Credentials) -> Tokens:
        ...

    @abstractmethod
    async def check_tokens(self, tokens: Tokens) -> bool:
        ...