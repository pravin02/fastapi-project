from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Album(Base):
    __tablename__ = "Album"
    albumId = Column(Integer, primary_key=True)
    title = Column(String)
    artistId = Column(Integer)

    def __init__(self, albumId: int, title: str, artistId: int):
        self.albumId = albumId
        self.title = title
        self.artistId = artistId

    def __call__(self, albumId: int, title: str):
        self.albumId = albumId
        self.title = title
        