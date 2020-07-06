from fastapi import APIRouter, Request, Form, Body
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from main.services import get_original_url, create_short_link
from pydantic import BaseModel

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get('/')
def main(request: Request):
    """Main page"""
    return templates.TemplateResponse("shortener.html", {
        "request": request,
        "message": "Hello World",
    })


class Url(BaseModel):
    url: str


@router.post("/shortify")
def shortify(url: Url = Body(...)):
    """Create short link for a given url"""
    short_link = create_short_link(url.url)
    return {"short_link": short_link}


@router.get('/{short_link}')
def redirect_to_original_url(short_link: str):
    """Redirect to original url using short link"""
    original_url = get_original_url(short_link)
    return RedirectResponse(original_url)
