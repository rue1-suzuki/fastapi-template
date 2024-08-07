import uvicorn
from fastapi import FastAPI

from routers.item_router import item_router

app = FastAPI()
app.include_router(router=item_router)


# uvicorn起動コマンド 本番用
if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="0.0.0.0",
        port=8000,
        reload=False,
    )
