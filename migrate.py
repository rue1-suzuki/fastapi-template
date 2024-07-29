from database import engine
from models.item_model import Base as ItemBase


def migrate():
    print("Creating item_tables")
    ItemBase.metadata.create_all(bind=engine)
    print("item_tables created")


if __name__ == "__main__":
    migrate()
