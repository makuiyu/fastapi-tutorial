from typing import Annotated, Any

from fastapi import Body, FastAPI, Path
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


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Annotated[Item | None, Body(embed=True)] = None,
):
    results: dict[str, Any] = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


@app.put("/items_user/{item_id}")
async def update_item_user(
    item_id: int,
    item: Annotated[Item, Body(embed=True)],
    user: Annotated[User, Body(embed=True)],
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    results: dict[str, Any] = {
        "item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results
