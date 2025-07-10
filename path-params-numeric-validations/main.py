from typing import Annotated, Any

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", gt=1, le=1000)],
    q: Annotated[str | None, Query(alias="item-query")] = None,
    size: Annotated[float | None, Query(gt=0.0, lt=10.0)] = None,
):
    results: dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if size:
        results.update({"size": size})
    return results
