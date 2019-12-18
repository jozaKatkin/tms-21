from sqlalchemy import Table, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from task_16_04.db_connects import Base

association_table = Table('association', Base.metadata,
                          Column('student_id', Integer, ForeignKey('student.id')),
                          Column('book_id', Integer, ForeignKey('book.id'))
                          )


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pages = Column(Integer)
    students = relationship('Student', secondary=association_table, backref='books')

    def __repr__(self):
        return f"id: {self.id}, Name: {self.name}, Pages: {self.pages}, Students: {self.students}"


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return f"id: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}"
