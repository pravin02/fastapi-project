from fastapi import APIRouter, Depends

from schemas.album import Album

from db.session import get_db_session
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter(prefix="/albums", tags=["albums"])


@router.get("", response_model=None)
def get_all_albums(db: Session = Depends(get_db_session)):
    return db.query(Album).all()