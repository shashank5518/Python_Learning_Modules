from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()

# @app.post("/items/")
# def create_item(item: Item):
#     item.name = "shashank"
#     item.description = "the best there is"
#     item.price = 99999999
#     item.tax = 0.10 * item.price
#     return item

# @app.post("/items/")
# def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax is not None:
#         price_with_tax = item.price + item.tax
#         item_dict.update(
#             {
#                 "price_with_tax": price_with_tax
#             }
#         )
#     return item_dict


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str | None = None):
    item_dict = item.model_dump()
    if item.tax is not None:
        # price_with_tax = item.price + item.tax
        # item_dict.update(
        #     {
        #         "price_with_tax": price_with_tax
        #     }
        # )
        item_dict["price_with_tax"] = item.price + item.tax
    result = {"item_id": item_id, **item_dict}
    if q:
        result.update({"q": q})
    return result
