from sqlalchemy.orm import sessionmaker
from Diary import Student, Diary
from task_16_03.db_connects import Base, engine

Base.metadata.create_all(engine)


def main():
    Session = sessionmaker(bind=engine)
    session = Session()

    student1 = Student(first_name="Meof", last_name="Purr")
    student2 = Student(first_name='Masha', last_name="Pur")
    student3 = Student(first_name='Vasya', last_name='Petrov')
    student4 = Student(first_name='Pasha', last_name='Kozlov')
    diary1 = Diary(gpu=9.0, student=student1)
    diary2 = Diary(gpu=5.0, student=student2)
    diary3 = Diary(gpu=7.8, student=student3)
    diary4 = Diary(gpu=4.9, student=student4)

    session.add_all([
        student1, student2, student3, student4,
        diary1, diary2, diary3, diary4
    ])
    session.commit()


if __name__ == '__main__':
    main()
