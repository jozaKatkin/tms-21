from classes import Math
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
        user_output = Math(x, y)
        if sign == '/':
            try:
                if y == 0:
                    raise ZeroDivisionError
            except ZeroDivisionError:
                print("Cannot divide by zero")
                continue
            output = user_output.divide(x, y)
        elif sign == '*':
            output = user_output.multi(x, y)
        elif sign == '+':
            output = user_output.plus(x, y)
        elif sign == '-':
            output = user_output.minus(x, y)
        print(f'{x} {sign} {y} = {output}')



