from db_connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    artist_id = Column(
        Integer, ForeignKey('artist.id'), nullable=False)

    artist = relationship(
        'Artist', foreign_keys='Album.artist_id', backref='albums')
