from sqlalchemy import Column, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship, backref

from task_16_03.db_connects import Base


class Diary(Base):
    __tablename__ = 'diary'
    id = Column(Integer, primary_key=True)
    gpu = Column(Float)

    student_id = Column(
        Integer, ForeignKey("student.id"), nullable=False
    )
    student = relationship(
        "Student",
        foreign_keys="Diary.student_id", backref=backref("diary", uselist=False)
    )

    def __repr__(self):
        return f"id: {self.id}, GPU: {self.gpu}"


class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return f"id: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}"
