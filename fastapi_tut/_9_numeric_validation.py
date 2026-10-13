from typing import Annotated

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=100)],
    size: Annotated[float, Query(gt=0, lt=10.5)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results


# Query() is for query parameter validation
# Path() is for path parameter validation
