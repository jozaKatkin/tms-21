from classes import Math
from exceptions import (
    BadCharError,
    Exit,
    WrongInputError
)

from config import CONFIG, EXIT


def choose():
    choice = int(input("Enter your choice: "))
    if not choice:
        return EXIT
    operation_data = CONFIG["operations"].get(choice)
    if not operation_data:
        raise WrongInputError
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    math = Math(x, y)
    res = getattr(math, operation_data["operation"])()
    print((operation_data["result_pattern"]).format(x, y, res))


def print_operations():
    print("Choose operation: ")
    operations = CONFIG["operations"]
    available_operations = sorted(CONFIG["available_operations"])
    list(map(lambda operation_code: print(operations[operation_code]['choice_message']), available_operations))
    

def ui():
    print("START")
    while True:
        print_operations()
        try:
            res = choose()
            if res == EXIT:
                break
        except Exception as err:
            print(err)
        input("press enter to continue\n")
