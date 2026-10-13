from typing import Any

from fastapi import FastAPI, Response, status
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    # username: str
    password: str
    # email: EmailStr
    # full_name: str | None = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None


# @app.post("/user/", response_model  = UserOut)
@app.post("/user/", status_code=status.HTTP_201_CREATED)
def create_user(user: UserIn) -> Any:
    return user


@app.get("/portal", response_model=None)
def get_portal(teleport: bool = False) -> Response | dict:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    # return JSONResponse(content={"message": "Here's your interdimensional portal."})
    return {"message": "Here's your interdimensional portal."}


@app.post("/items/", response_model=Item, response_model_exclude_unset=True)
def create_item(item: Item) -> Any:
    return item


@app.get("/items/", response_model=list[Item])
def read_items() -> Any:
    return [
        Item(name="Portal Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]


@app.get(
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include={"name", "description"},
)
def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
def read_item_public_data(item_id: str):
    return items[item_id]
