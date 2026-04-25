from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

"""Artist entity"""
class Artist(Base):
    __tablename__ = "Artist"   
    artistId = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, artistId: int, name: str):
        self.artistId = artistId
        self.name = name