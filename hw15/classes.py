from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///database0.db", echo=True)
metadata = MetaData()
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    amount = Column(Integer)

    def __init__(self, id_, name, price, amount):
        self.id_ = id_
        self.name = name
        self.price = price
        self.amount = amount

    def __repr__(self):
        return "PRODUCT: %r, %r, %r" % (
            self.name, self.price, self.amount
        )


Base.metadata.create_all(engine)

