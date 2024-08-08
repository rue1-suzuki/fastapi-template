import logging
from uuid import UUID

from fastapi import Depends, HTTPException, Path
from sqlalchemy.orm import Session

from dependencies.get_db import get_db
from schemas.item_schema import ItemSchema
from utils.get_item_or_404 import get_item_or_404


def get_item(
    uuid: UUID = Path(),
    db: Session = Depends(get_db),
) -> ItemSchema:
    try:
        item = get_item_or_404(
            uuid=uuid,
            db=db,
        )

        return ItemSchema.model_validate(item)
    except HTTPException as e:
        raise e
    except Exception as e:
        logging.error(e)
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
