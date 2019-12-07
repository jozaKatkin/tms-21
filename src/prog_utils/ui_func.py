from func import (
plus,
minus,
multi,
divide
)

from exceptions import (
BadCharError,
Exit
)


def my_calc():
    while True:
        try:
            x = float(input('x: '))
            y = float(input('y: '))
        except ValueError:
            print("Type in only numbers")
            continue
        sign = input('sign: ')
        if sign == '0':
            raise Exit
        try:
            if sign not in ['+', '-', '*', '/']:
                raise BadCharError
        except BadCharError:
            print("Wrong input\n+, -, *, / signs expected")
            continue
        if sign == '/':
            try:
                if y == 0:
                    raise ZeroDivisionError
            except ZeroDivisionError:
                print("Cannot divide by zero")
                continue
            z = x / y
        elif sign == '*':
            z = x * y
        elif sign == '+':
            z = x + y
        elif sign == '-':
            z = x - y
        print(f'{x} {sign} {y} = {z}')

