from fastapi import APIRouter, Depends

from schemas.artist import Artist

from db.session import get_db_session
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter(prefix="/artists", tags=["albums"])


@router.get("")
def get_all_artists(session: Session = Depends(get_db_session)):
    """artist api return all the artists"""
    return session.query(Artist).all()


@router.get("/{artistId}")
def get_artist_by_id(artistId: int, session: Session = Depends(get_db_session)):
    """Get artist by artistId"""
    return session.get(Artist, artistId)
