from typing import Annotated, Any

from fastapi import FastAPI, Query

app = FastAPI()

# @app.get("/items/")
# def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50)] = None):
#     results: dict[str, Any] = {
#         "items": [
#             {
#                 "item_id": "Foo"
#             },
#             {
#                 "item_id": "Bar"
#             }
#         ]
#     }
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# # def read_items(q: Annotated[list[str] | None, Query()] = None):
# def read_items(q: Annotated[list[str], Query()] = ["foo", "bar", "baz", "ball"]):
#     query_items= {"q": q}
#     return query_items

# @app.get("/items/")
# def read_items(
#     q: Annotated[str | None, Query(title = "Query String", description = "Query string for the items to search in the database that have a good match", min_length=3)] = None,
# ):
#     results = {"items": [{"item_id": "foo"}, {"item_id": "bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


@app.get("/items/")
def read_items(
    q: Annotated[
        str | None, Query(alias="item-query", deprecated=True, include_in_schema=False)
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# alternate method, not annotated
# def read_items(q: str | None = Query(default=None, max_length=50)):
