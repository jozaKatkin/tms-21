class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figures:
    def __init__(self, name):
        self.name = name


class Square(Figures):
    def __init__(self, point1, point2, name):
        super().__init__(name)
        self.point1 = point1
        self.point2 = point2

    def find_length(self):
        length = (((self.point2.y - self.point1.y) ** 2) + ((self.point2.x - self.point1.x) ** 2)) ** 0.5
        return length

    def find_perimeter(self):
        diagonal = self.find_length()
        perimeter = 2 * (2 ** 0.5) * diagonal
        return round(perimeter, 3)

    def find_square(self):
        d = self.find_length()
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
        ab = (((self.a.y - self.b.y) ** 2) + ((self.a.x - self.b.x) ** 2)) ** 0.5
        bc = (((self.b.y - self.c.y) ** 2) + ((self.b.x - self.c.x) ** 2)) ** 0.5
        ca = (((self.c.y - self.a.y) ** 2) + ((self.c.x - self.a.x) ** 2)) ** 0.5
        return ab, bc, ca

    def find_perimeter(self):
        ab, bc, ca = self.find_sides()
        p = ab + bc + ca
        return round(p, 3)

    def find_square(self):
        s = 0.5 * (abs(((self.b.x - self.a.x) * (self.c.y - self.a.y)) -
                       ((self.c.x - self.a.x) * (self.b.y - self.a.y))))
        return round(s, 3)
