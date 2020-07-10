from fastapi import APIRouter
from app.main.services import create_short_link, get_original_url

api_router = APIRouter()


@api_router.post('/shortify')
async def shortify_url(url: str):
    """Gives short link for a full url"""
    short_link = await create_short_link(url)
    return {"short_link": short_link}


@api_router.get('/get_original')
async def restore_url(link: str):
    """Gives full url for a short link"""
    original_url = await get_original_url(link)
    return {"original_url": original_url}
