class WrongInputError(Exception):
    def __init__(self, message="Type in valid operation number"):
        super().__init__(message)


class WrongColonError(Exception):
    def __init__(self, message="No such a colon"):
        super().__init__(message)


class WrongIdError(Exception):
    def __init__(self, message="No such id"):
        super().__init__(message)


class WrongValueError(Exception):
    def __init__(self, message="amount - type float not expected"):
        super().__init__(message)