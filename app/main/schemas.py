from pydantic import BaseModel


class Url(BaseModel):
    url: str


class LinkBase(BaseModel):
    link: str


class LinkCreate(LinkBase):
    url: str


class Link(LinkBase):
    class Config:
        orm_mode = True
