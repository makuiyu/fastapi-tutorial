from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump(exclude_unset=True)
    return item_dict


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}
