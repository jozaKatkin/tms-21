class BadCharError(Exception):
    def __init__(self, message="Wrong sign"):
        super().__init__(message)


class Exit(Exception):
    def __init__(self, message="Buy!"):
        super().__init__(message)


class WrongInputError(Exception):
    def __init__(self, message="Wrong input"):
        super().__init__(message)