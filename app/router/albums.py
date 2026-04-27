from fastapi import APIRouter, Depends

from schemas.album import Album
from schemas.artist import Artist

from models.album_dto import AlbumDto

from db.session import get_db_session
from sqlalchemy import select
from sqlalchemy.orm import Session

router = APIRouter(prefix="/albums", tags=["albums"])


@router.get("")
def get_all_albums(session: Session = Depends(get_db_session)):
    """Albums api return all the albums"""
    dtos = []
    for row in session.query(Album).all():
        dtos.append(AlbumDto(row.albumId, row.title))    
    return dtos



@router.get("/{albumId}")
def get_album_by_id(albumId: int, session: Session = Depends(get_db_session)):
    """Get album by albumId"""
    return (
        session.get(Album, albumId)
    )


@router.get("/with_artists")
def get_albums_with_artists(session: Session = Depends(get_db_session)):
    """Get album with artists"""
    return session.execute(select(Album, Artist).group_by("artistId")).scalars().all()
