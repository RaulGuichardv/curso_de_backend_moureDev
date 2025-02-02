from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   responses={404: {"message": "no se encontro el producto"}},
                   tags=["products"])

products_list = ["producto 1", "producto 2", "producto 3", "producto 4", "producto 5",]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id: int):
    return products_list[id] if len(products_list) > id else "el productos no existe"