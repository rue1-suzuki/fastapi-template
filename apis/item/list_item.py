from fastapi import Depends
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from models.item_model import Item
from schemas.item_schema import ItemSchema


def list_item(
    db: Session = Depends(get_db),
) -> list[ItemSchema]:
    items = db.query(Item).all()

    return [ItemSchema.model_validate(item) for item in items]
