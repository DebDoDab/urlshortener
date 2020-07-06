from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from services import get_original_url, get_short_link

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get('/')
def main(request: Request):
    return templates.TemplateResponse("main.html", {
        "request": request,
        "message": "Hello World",
    })


@router.post('/shortify')
def shortify_link(url: str):
    short_link = get_short_link(url)
    return {"short_link": short_link}


@router.get('/{short_link}')
def redirect_to_original_url(short_link: str):
    original_url = get_original_url(short_link)
    return RedirectResponse(original_url)