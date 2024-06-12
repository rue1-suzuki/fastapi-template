from fastapi import FastAPI

from migrate import migrate
from routers.item_router import item_router

migrate()

app = FastAPI()
app.include_router(router=item_router)
