from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from routers import products, user, users, jwt_auth_users, users_db
app = FastAPI()

# Routers
app.mount("/static", StaticFiles(directory="static"),name="static")
app.include_router(products.router)
app.include_router(user.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)

@app.get("/")
async def root():
    return "hola"

@app.get("/url")
async def url():
    return {"url": "https://google.com"} 

# uvicorn main:app --reload