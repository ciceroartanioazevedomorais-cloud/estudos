from typing import List
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.exceptions import InvalidAgeException
from app.schemas.user import UserCreate

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, user_data: UserCreate) -> User:
        if user_data.age < 0:
            raise InvalidAgeException()

        user = User(name=user_data.name, age=user_data.age)
        return self.user_repository.create(user)

    def get_users(self) -> List[User]:
        return self.user_repository.get_all()
