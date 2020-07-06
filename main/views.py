from fastapi import APIRouter, Request, Body, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from main.services import get_original_url, create_short_link
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get('/')
def main(request: Request):
    """Main page"""
    return templates.TemplateResponse("shortener.html", {
        "request": request,
        "message": "Hello World",
    })


@router.post("/shortify")
def shortify(url: schemas.Url = Body(...), db: Session = Depends(get_db)):
    """Create short link for a given url"""
    short_link = create_short_link(db, url.url)
    return {"short_link": short_link}


@router.get('/{short_link}')
def redirect_to_original_url(short_link: str, db: Session = Depends(get_db)):
    """Redirect to original url using short link"""
    original_url = get_original_url(db, short_link)
    return RedirectResponse(original_url)
