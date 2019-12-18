from sqlalchemy import Column, Integer, String
from db_connection import Base


class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String)
