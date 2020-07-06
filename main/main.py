from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from main.views import router
from api.views import api_router
from .database import SessionLocal, engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(api_router, prefix="/api")
app.include_router(router)
