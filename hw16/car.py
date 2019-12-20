from hw16.db_connections import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String)
    release_year = Column(Integer)
    brand_id = Column(
        Integer, ForeignKey('brand.id'), nullable=False)

    brand = relationship(
        'Brand', lazy='subquery', foreign_keys='Car.brand_id', backref='cars')

    def __repr__(self):
        return f'id: {self.id}, Model: {self.model}, Year: {self.release_year}, {self.brand}'
