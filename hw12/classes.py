class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figures:
    def __init__(self, name):
        self.name = name

    def find_length(self, point1, point2):
        length = (((point2.y - point1.y) ** 2) + ((point2.x - point1.x) ** 2)) ** 0.5
        return length


class Square(Figures):
    def __init__(self, point1, point2, name):
        super().__init__(name)
        self.point1 = point1
        self.point2 = point2

    def find_perimeter(self):
        diagonal = self.find_length(self.point1, self.point2)
        perimeter = 2 * (2 ** 0.5) * diagonal
        return round(perimeter, 3)

    def find_square(self):
        d = self.find_length(self.point1, self.point2)
        s = 0.5 * (d ** 2)
        return round(s, 3)


class Circle(Figures):
    def __init__(self, center, radius, name):
        super().__init__(name)
        self.center = center
        self.radius = radius

    def find_perimeter(self):
        p = 2 * 3.1415 * self.radius
        return round(p, 3)

    def find_square(self):
        s = 3.1415 * (self.radius ** 2)
        return round(s, 3)


class Triangle(Figures):
    def __init__(self, a, b, c, name):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c

    def find_sides(self):
        ab = self.find_length(self.a, self.b)
        bc = self.find_length(self.b, self.c)
        ca = self.find_length(self.b, self.c)
        return ab, bc, ca

    def find_perimeter(self):
        ab, bc, ca = self.find_sides()
        p = ab + bc + ca
        return round(p, 3)

    def find_square(self):
        s = 0.5 * (abs(((self.b.x - self.a.x) * (self.c.y - self.a.y)) -
                       ((self.c.x - self.a.x) * (self.b.y - self.a.y))))
        return round(s, 3)
