class WrongInputError(Exception):
    def __init__(self, message="Wrong input"):
        super().__init__(message)
