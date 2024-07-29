from fastapi import FastAPI

from routers.item_router import item_router

app = FastAPI()
app.include_router(router=item_router)
