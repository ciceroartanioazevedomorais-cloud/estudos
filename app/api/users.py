from typing import List
from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository

router = APIRouter()

# Dependency injection
# In a real app, this might be handled by a DI container or a global state
user_repository = UserRepository()

def get_user_service() -> UserService:
    return UserService(user_repository)

@router.post("/users", response_model=UserResponse)
def create_user(user_data: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user_data)

@router.get("/users", response_model=List[UserResponse])
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()
