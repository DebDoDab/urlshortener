from decouple import config
import random
import string
from typing import Union
from . import models

POSSIBLE_CHARS = string.ascii_letters + string.digits


async def get_host_name():
    """Read HOST_NAME variable from .env file or make it default"""
    host_name = config("HOST_NAME")
    if host_name is None:
        host_name = "localhost:8000/"
    return host_name


async def get_original_url(short_link: str) -> Union[str, None]:
    """Return a full url for a given short link or return None if it doesn't exists"""
    resp = await models.Link.find_by_link(short_link)
    return resp['url'] if resp else None


async def create_short_link(url: str) -> str:
    """Create and return short link for a given full url"""
    host_name = await get_host_name()

    db_link = await models.Link.find_by_url(url)
    if db_link:
        return host_name + db_link['link']

    short_link = "".join(random.choices(POSSIBLE_CHARS, k=5))
    while await get_original_url(short_link):
        short_link = "".join(random.choices(POSSIBLE_CHARS, k=5))

    await models.Link.create(url, short_link)

    return host_name + short_link
