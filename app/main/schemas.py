from pydantic import BaseModel


class Url(BaseModel):
    """FastAPI schema for getting URL"""
    url: str


class LinkBase(BaseModel):
    """Base schema for returning Link in JSON"""
    link: str


class LinkCreate(LinkBase):
    """Schema for returning Link in JSON after it creation"""
    url: str


class Link(LinkBase):
    """Schema for returning link in JSON"""
    class Config:
        orm_mode = True
