# import sqlite3
# SQLITE_DB_PATH = "C:/Users/Hp/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db"
# connection =sqlite3.connect(SQLITE_DB_PATH)

# cursor = connection.cursor();
# cursor.execute("SELECT * FROM Album")

# for row in cursor.fetchall():
#     print(row[1])

# connection.close()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLITE_DB_PATH = "sqlite:///C:/Users/Hp/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db"
engine = create_engine(SQLITE_DB_PATH);
Base = declarative_base()

# Define table using ORM
class Album(Base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(String)

# Create tables
Base.metadata.create_all(engine)

# Create session to interact with database
session = sessionmaker(bind=engine)
session = session()

albums = session.query(Album).all()

for album in albums:
    print(f"AlbumId:{album.AlbumId}, Title: {album.Title} ArtistsId: {album.ArtistId}")



