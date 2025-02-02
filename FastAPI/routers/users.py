from fastapi import APIRouter
from pydantic import BaseModel

from routers.user import users_list
from routers.user import User

router = APIRouter(prefix="/users",
                   tags=["users"])

@router.get("/")
async def users():
    return users_list
