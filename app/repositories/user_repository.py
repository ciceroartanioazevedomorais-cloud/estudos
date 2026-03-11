from typing import List
from app.models.user import User

class UserRepository:
    def __init__(self):
        self._users: List[User] = []

    def create(self, user: User) -> User:
        self._users.append(user)
        return user

    def get_all(self) -> List[User]:
        return self._users
