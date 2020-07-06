from fastapi import Request, Response, APIRouter, Depends
from main.services import create_short_link, get_original_url
from main.database import get_db
from sqlalchemy.orm import Session

api_router = APIRouter()


@api_router.post('/shortify')
def shortify_url(url: str, db: Session = Depends(get_db)):
    """Gives short link for a full url"""
    short_link = create_short_link(db, url)
    return {"short_link": short_link}


@api_router.get('/get_original')
def restore_url(link: str, db: Session = Depends(get_db)):
    """Gives full url for a short link"""
    original_url = get_original_url(db, link)
    return {"original_url": original_url}
