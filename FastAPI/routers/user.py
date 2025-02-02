from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/user",
                   tags=["user"])
class User(BaseModel):
    id: int
    name: str
    password: str



users_list = [User(id = 0, name = "raul", password =  "contraseña"),
              User(id = 1, name = "yoyo", password =  "primarikey"),
              User(id = 2, name = "culo", password =  "caca")]

@router.get("/{id}")  
async def user(id: int):
    return searchUser(id)

@router.post("/")
async def createUser(user: User):
    if type(searchUser(user.id)) != User:
        users_list.routerend(user)
        return user
    return "ese ya esta we"

@router.put("/")
async def updateUser(user: User):
    for index, userList in enumerate(users_list):
        if userList.id == user.id:
            users_list[index] = user
            return user
    return "no se pudo actualizar el usuario"

@router.delete("/{id}")
async def deleteUser(id: int):
    for index, userList in enumerate(users_list):
        if userList.id == id:
            del users_list[index]
            return "se elimino el usuario"
    return "no se pudo actualizar el usuario"

def searchUser(id: int):
    for user in users_list:
        if user.id == id:
            return user
    return None