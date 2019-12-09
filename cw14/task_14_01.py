from time import sleep
from random import randint


def my_generator(a, b, diff):
    while True:
        sleep(1)
        yield randint(a, b)
        a += diff
        b += diff


gener = my_generator(1, 10, 10)

print(next(gener))

for i in gener:
    print(i)
