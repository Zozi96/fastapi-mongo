from pydantic import constr, EmailStr, BaseModel

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
