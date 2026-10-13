from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    # tags: list[str] = []
    tags: set[str] = set()
    images: list[Image] | None = None
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


class Offer(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["a very nice item"])
    price: float = Field(examples=[35.4])
    items: list[Item]

    # {
    #     "name": "Foo",
    #     "description": "The pretender",
    #     "price": 42.0,
    #     "tax": 3.2,
    #     "tags": ["rock", "metal", "bar"],
    #     "image": {
    #         "url": "http://example.com/baz.jpg",
    #         "name": "The Foo live"
    #     }
    # }

    # {
    #     "name": "Foo",
    #     "description": "The pretender",
    #     "price": 42.0,
    #     "tax": 3.2,
    #     "tags": [
    #         "rock",
    #         "metal",
    #         "bar"
    #     ],
    #     "images": [
    #         {
    #             "url": "http://example.com/baz.jpg",
    #             "name": "The Foo live"
    #         },
    #         {
    #             "url": "http://example.com/dave.jpg",
    #             "name": "The Baz"
    #         }
    #     ]
    # }


@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": Annotated}
    return results


@app.post("/offers/")
def create_offer(offer: Offer):
    return offer


@app.post("/images/multiple/")
def create_multiple_images(images: list[Image]):
    return images
