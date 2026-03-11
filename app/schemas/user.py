from pydantic import BaseModel, Field

class UserBase(BaseModel):
    name: str
    age: int

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    pass
