from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.main.views import router
from app.api.views import api_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(api_router, prefix="/api")
app.include_router(router)
