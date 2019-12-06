from classes import Point, Circle, Triangle, Square


def main():
    point1 = Point(4, 2)
    point2 = Point(8, 8)
    square = Square(point1, point2, "square")
    #
    point3 = Point(10, 2)
    triangle = Triangle(point1, point2, point3, "triangle")
    #
    circle = Circle(4, 5, "circle")

    def count_figures(figures):
        for figure in figures:
            p = figure.find_perimeter()
            s = figure.find_square()
            print(f"{figure.name}: P = {p}, S = {s}")

    my_figures = [square, triangle, circle]
    count_figures(my_figures)


if __name__ == "__main__":
    main()
