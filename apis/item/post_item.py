from fastapi import Body, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from models.item_model import Item
from schemas.item_schema import ItemSchema


class RequestBody(BaseModel):
    name: str = Field(
        min_length=1,
        max_length=255,
    )
    price: float = Field(
        ge=0,
    )


def post_item(
    body: RequestBody = Body(),
    db: Session = Depends(dependency=get_db),
) -> ItemSchema:
    item = Item()
    item.name = body.name
    item.price = body.price
    db.add(item)
    db.commit()
    db.refresh(item)

    return ItemSchema.model_validate(item)
