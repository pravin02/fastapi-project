from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

SQLITE_DB_PATH = "sqlite:///database/Chinook.db"
engine = create_engine(
    url=SQLITE_DB_PATH, pool_pre_ping=True, pool_size=20, max_overflow=0
)

Base = declarative_base()

session = sessionmaker(bind=engine, expire_on_commit=False)


def get_db_session() -> Session:
    """Return the database session"""
    return session()
