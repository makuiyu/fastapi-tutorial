from typing import Annotated, Any

from fastapi import FastAPI, Query

app = FastAPI()


# @app.get("/items/")
# async def read_items(
#     q: Annotated[str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")] = 'fixedquery'
# ):
#     results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = []):
#     query_items = {"q": q}
#     return query_items


@app.get("/items/")
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            pattern="^fixedquery$",
            min_length=3,
            max_length=50,
            deprecated=True,
        ),
    ] = None,
):
    results: dict[str, Any] = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
