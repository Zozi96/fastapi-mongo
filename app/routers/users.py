from typing import List
from fastapi import APIRouter, Body, Request, HTTPException, status, encoders

from app.models.users import UserResponseSchema, UserCreateSchema
from app.security import password_hash
from app.database import user_collection
from app.utils import get_object_id

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    path="/",
    response_model=List[UserResponseSchema],
    response_description="List all users",
)
async def get_users(request: Request) -> List[UserResponseSchema]:
    users = await user_collection.find({}).to_list(length=100)
    return users


@router.get(
    path="/{id}",
    response_model=UserResponseSchema,
    response_description="Get a single user",
)
async def get_user(id: str, request: Request) -> UserResponseSchema | None:
    object_id = await get_object_id(id)
    user = await user_collection.find_one({"_id": object_id})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User {id} not found"
        )
    return user


@router.post(
    path="/",
    response_model=UserResponseSchema,
    response_description="Create a new user",
)
async def create_user(user: UserCreateSchema = Body()) -> UserResponseSchema:
    user_data: dict = encoders.jsonable_encoder(user)
    user_data["password"] = await password_hash(user_data["password"])
    new_user = await user_collection.insert_one(user_data)
    created_user = await user_collection.find_one({"_id": new_user.inserted_id})
    return created_user
