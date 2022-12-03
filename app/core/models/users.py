from pydantic import constr, EmailStr, BaseModel, validator

from core.database import user_collection
from core.models import BaseSchema


class UserResponseSchema(BaseSchema):
    username: str
    email: EmailStr
    first_name: str | None
    last_name: str | None


class UserCreateSchema(BaseModel):
    username: constr(min_length=4, max_length=20)
    email: EmailStr
    password: constr(min_length=8, max_length=20)
    first_name: str | None
    last_name: str | None

    @validator("username")
    def username_exists(cls, value):
        if user_collection.find_one({"username": value}):
            raise ValueError("Username already exists")
        return value

    @validator("email")
    def email_exists(cls, value):
        if user_collection.find_one({"email": value}):
            raise ValueError("Email already exists")
        return value
