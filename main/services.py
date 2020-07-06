from typing import Union
import random
import string
from sqlalchemy.orm import Session
import sys
from . import models, schemas

LETTERS = string.ascii_letters + string.digits


def get_original_url(db: Session, short_link: str) -> Union[str, None]:
    """Return a full url for a given short link or return None if it doesn't exists"""
    resp = db.query(models.Link).filter(models.Link.link == short_link).first()
    return resp.url if resp else None


def create_short_link(db: Session, url: str) -> str:
    """Create and return short link for a given full url"""
    if short_link := db.query(models.Link).filter(models.Link.url == url).first():
        return short_link

    short_link = "".join(random.choices(LETTERS, k=5))
    while get_original_url(db, short_link):
        short_link = "".join(random.choices(LETTERS, k=5))

    db_link = models.Link(link=short_link, url=url)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)

    # TODO add variable instead of "localhost:8000/"
    return "localhost:8000/" + short_link
