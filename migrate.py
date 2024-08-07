import logging

from database import engine
from models.item_model import Base as ItemBase


def migrate():
    logging.warning("item_model migration")
    ItemBase.metadata.create_all(bind=engine)

    logging.warning("migration complete")


if __name__ == "__main__":
    migrate()
