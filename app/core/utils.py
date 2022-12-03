from bson import ObjectId, errors

from fastapi import HTTPException, status

async def get_object_id(id: str) -> ObjectId:
    try:
        return ObjectId(id)
    except errors.InvalidId:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalide id {id}")