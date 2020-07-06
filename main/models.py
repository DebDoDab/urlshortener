from sqlalchemy import Column, Integer, String
from .database import Base


class Link(Base):
    """Model for storing link between short link and full url"""
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True)
    link = Column(String, unique=True)
