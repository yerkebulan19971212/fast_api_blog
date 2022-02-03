from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    username: str
    email: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/user/{user_id}/", response_model=User)
async def say_hello(user_id: int):
    user = {
        "id": 2,
        "username": "yerkebulan",
        "email": "yerkebulan@gmail.com"
    }
    return user
