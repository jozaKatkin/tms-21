from sqlalchemy import Column, Integer, String

from hw16.db_connections import Base


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f'Brand: {self.name}'
