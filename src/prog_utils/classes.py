from func import validate_args


class Math:
    def __init__(self, num1, num2):
        validate_args(num1, num2)
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        return self.num1 + self.num2

    def minus(self):
        return self.num1 - self.num2

    def multi(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

