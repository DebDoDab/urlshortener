from typing import Optional
from .database import BaseMongoCRUD
from bson import ObjectId


class Link(BaseMongoCRUD):
    collection = "List"

    @classmethod
    async def create(cls, url: str, link: str) -> ObjectId:
        return (await super().insert_one(await cls.to_dict(url, link))).inserted_id

    @classmethod
    async def find_by_link(cls, link: str) -> Optional[dict]:
        return await super().find_one({"link": link})

    @classmethod
    async def find_by_url(cls, url: str) -> Optional[dict]:
        return await super().find_one({"url": url})

    @classmethod
    async def to_dict(cls, url: str, link: str) -> dict:
        return {"url": url, "link": link}
