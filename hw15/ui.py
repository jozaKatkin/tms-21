from config import (
    CONFIG,
    EXIT,
)
from exceptions import (
    WrongInputError,
)


def print_funcs():
    funcs = CONFIG["functions"]
    available_funcs = sorted(CONFIG["available_functions"])
    list(map(lambda func_code: print(funcs[func_code]["choice_message"]), available_funcs))


def print_divider():
    print("*" * 15)


def press_enter():
    print_divider()
    input("Press ENTER to continue\n")
    print_divider()


def start_message():
    print_divider()
    print("Start")
    print_divider()


def end_message():
    print_divider()
    print("See you soon")
    print_divider()


def ui():
    start_message()
    while True:
        print_funcs()
        print_divider()
        try:
            choice = int(input("Choose function:\n"))
            if choice == EXIT:
                end_message()
                break
            func_data = CONFIG["functions"].get(choice)
            if not func_data:
                raise WrongInputError
            args = input(func_data["input_message"])
            func_data["function"](args)
        except Exception as err:
            print_divider()
            print(err)
        press_enter()


