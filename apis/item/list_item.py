import logging

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from models.item_model import Item
from schemas.item_schema import ItemSchema


def list_item(
    db: Session = Depends(get_db),
) -> list[ItemSchema]:
    try:
        items = db.query(Item).all()

        return [ItemSchema.model_validate(item) for item in items]
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
