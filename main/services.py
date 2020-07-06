import os
import random
import string
from typing import Union
from sqlalchemy.orm import Session
from . import models

POSSIBLE_CHARS = string.ascii_letters + string.digits


def get_original_url(db: Session, short_link: str) -> Union[str, None]:
    """Return a full url for a given short link or return None if it doesn't exists"""
    resp = db.query(models.Link).filter(models.Link.link == short_link).first()
    return resp.url if resp else None


def create_short_link(db: Session, url: str) -> str:
    """Create and return short link for a given full url"""
    if db_link := db.query(models.Link).filter(models.Link.url == url).first():
        return db_link.link

    short_link = "".join(random.choices(POSSIBLE_CHARS, k=5))
    while get_original_url(db, short_link):
        short_link = "".join(random.choices(POSSIBLE_CHARS, k=5))

    db_link = models.Link(link=short_link, url=url)
    db.add(db_link)
    db.commit()
    db.refresh(db_link)

    host_name = os.getenv("HOST_NAME")
    if host_name is None:
        host_name = "localhost:8000/"
    return host_name + short_link
