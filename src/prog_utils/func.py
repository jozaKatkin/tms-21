from exceptions import WrongInputError


def validate_args(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        message = f"Arguments should be int or float. Now it is {type(x)}, {type(y)}.\n"
        raise WrongInputError(message)