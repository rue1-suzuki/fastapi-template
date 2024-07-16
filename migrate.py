from database import Base, engine


def migrate():
    Base.metadata.create_all(
        bind=engine,
    )


if __name__ == "__main__":
    migrate()
