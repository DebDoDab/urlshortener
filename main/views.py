from fastapi import APIRouter, Request, Body, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from main.services import get_original_url, create_short_link, get_host_name
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get('/')
async def main(request: Request):
    """Main page"""
    host_name = await get_host_name()
    return templates.TemplateResponse("shortener.html", {
        "request": request,
        "HOST_NAME": host_name,
    })


@router.post("/shortify")
async def shortify(url: schemas.Url = Body(...), db: Session = Depends(get_db)):
    """Create short link for a given url"""
    short_link = await create_short_link(db, url.url)
    return {"short_link": short_link}


@router.get('/{short_link}')
async def redirect_to_original_url(short_link: str, db: Session = Depends(get_db)):
    """Redirect to original url using short link"""
    original_url = await get_original_url(db, short_link)
    return RedirectResponse(original_url)
