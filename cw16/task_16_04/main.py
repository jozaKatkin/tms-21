from sqlalchemy.orm import sessionmaker
from Book import Book, Student
from task_16_04.db_connects import Base, engine

Base.metadata.create_all(engine)


def main():
    Session = sessionmaker(bind=engine)
    session = Session()

    student1 = Student(first_name='Pasha', last_name="Kotov")
    student2 = Student(first_name='Masha', last_name="Pur")
    student3 = Student(first_name='Vasya', last_name='Petrov')
    student4 = Student(first_name='Pasha', last_name='Kozlov')
    students = [student1, student2, student3, student4]
    book1 = Book(name='Good book', pages=30, students=students)
    book2 = Book(name='Bad book', pages=40, students=students)
    book3 = Book(name='Cool book', pages=100, students=students)
    book4 = Book(name='Mathematics', pages=78, students=students)
    book5 = Book(name='English', pages=56, students=students)
    books = [book1, book2, book3, book4, book5]
    combo_list = students + books
    session.add_all(combo_list)
    session.commit()


if __name__ == '__main__':
    main()
