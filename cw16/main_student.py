from sqlalchemy.orm import sessionmaker
from group import Group
from db_connection import Base, engine
from student import Student

Base.metadata.create_all(engine)


def main():
    Session = sessionmaker(bind=engine)
    session = Session()

    group = Group(name="Z-21")
    student = Student(firstname='Pasha', lastname='Ivanov', group=group)
    session.add_all([group, student])
    session.commit()


if __name__ == '__main__':
    main()
