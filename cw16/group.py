from sqlalchemy import Column, Integer, String
from db_connection import Base


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'id: {self.id} Name: {self.name}'




