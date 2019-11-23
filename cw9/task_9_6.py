# Написать декоратор, который будет выводить время выполнения функции

from datetime import datetime


def my_decorator(func):
    def do_some_staff():
        time1 = datetime.now()
        func()
        time2 = datetime.now()
        delta = time2 - time1
        print(delta)

    return do_some_staff


@my_decorator
def my_func():
    pass


my_func()
