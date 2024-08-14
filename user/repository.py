from Repo.AbstractRepository import AbstractSQLAlchemyRepository
from user.schemas import UserUpdate, UserCreate, UserResponse
from user.models import User


class UserRepo(
    AbstractSQLAlchemyRepository[
        User,
        UserResponse,
        UserCreate,
        UserUpdate,
    ]
):
    def entity_to_model(self, entity: User) -> UserResponse:
        return UserResponse(
            id=entity.id,
            email=entity.email,
            hash_password=entity.hash_password,
            tags=entity.tags,
        )

    def model_to_entity(self, model: UserResponse) -> User:
        return User(
            email=model.email,
            hash_password=model.hash_password,
        )
