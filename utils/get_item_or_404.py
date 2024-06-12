from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.item_model import Item


def get_item_or_404(uuid: UUID, db: Session):
    item = db.get(
        entity=Item,
        ident=uuid,
    )

    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
        )

    return item
