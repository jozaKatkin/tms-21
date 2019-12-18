from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from db_connection import Base


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    group_id = Column(
        Integer, ForeignKey('group.id'), nullable=False)

    group = relationship(
        'Group', foreign_keys='Student.group_id', backref='students')