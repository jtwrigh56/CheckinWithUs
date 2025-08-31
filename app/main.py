from fastapi import fastapi
from app.database import db


app =  fastapi()

@app.get("/")
async def root():
    return {"message": "Hello from Railway + FastAPI + MongoDB"}

@app.get("/users")
async def get_users():
    users = await db.users.find().to_list(100)
    return users

@app.post("/users")
async def create_user(user: dict):
    result = await db.users.insert_one(user)
    return {"id": str(result.inserted_id)}