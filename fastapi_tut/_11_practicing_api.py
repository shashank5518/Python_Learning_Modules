from typing import Annotated

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


# @app.put("/items/{item_id}")
# def update_item(
#     item_id: Annotated[int, Path(title="ID of the item to get", ge = 0, le = 1000)],
#     item: Item,
#     user: User,
#     q: str | None = None,
# ):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results


@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Annotated[Item, Body(embed=True)],
    user: User,
    importance: Annotated[int, Body()],
    q: str | None = None,
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
