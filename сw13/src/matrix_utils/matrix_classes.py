from random import randint


class Matrix:
    def __init__(self, data=None, n=5, m=5, a=0, b=0):
        if data is None:
            matrix = []
            for i in range(n):
                line = []
                for j in range(m):
                    line.append(randint(a, b))
                matrix.append(line)
            self.data = matrix
        else:
            self.data = data
            self.n = n
            self.m = m
            self.a = a
            self.b = b

    def __str__(self):
        return f"matrix: \n{self.data}"

