from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from db.client import client
from db.schemes.user import user_scheme, users_scheme
from db.models.user import User
router = APIRouter(prefix="/usersdb",
                   tags=["UsersDB"])

db = client.grupo.users

@router.get("")
async def users():
    return users_scheme(db.find())


@router.get("/{id}")
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.post("")
async def create_user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="el usuario ya existe ")
    user = dict(user)
    del user["id"]
    id = db.insert_one(user).inserted_id
    new_user = user_scheme(db.find_one({"_id": id}))
    return User(**new_user)


@router.put("")
async def update_user(user: User):
    user_dict = dict(user)
    del user_dict["id"]
    try:
        db.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"Error": "no se pudo actualizar el usuario"}

    return search_user({"_id": ObjectId(user.id)})

@router.delete("/{id}")
async def delete_user(id: str):
    found = db.find_one_and_delete({"_id": ObjectId(id)})
    return User(**user_scheme(found))
    if not found:
        return {"error": "No se ha eliminado el usuario"}


def search_user(key: str, value):
    try:
        user = db.find_one({key: value})
        return User(**user_scheme(user))
    except:
        return {"Error": "no se encontro el usuario"}