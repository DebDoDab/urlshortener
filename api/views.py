from fastapi import Request, Response, APIRouter
from main.services import create_short_link, get_original_url

api_router = APIRouter()


@api_router.post('/shortify')
def shortify_url(url: str):
    """Gives short link for a full url"""
    short_link = create_short_link(url)
    return {"short_link": short_link}


@api_router.get('/get_original')
def restore_url(link: str):
    """Gives full url for a short link"""
    original_url = get_original_url(link)
    return {"original_url": original_url}
