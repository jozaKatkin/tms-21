from math import sqrt


def count_equation(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif d == 0:
        x = (-b + sqrt(d)) / (2 * a)
        print(x)
    else:
        print("Корней нет")


def main():
    count_equation(1, 2, 3)


if __name__ == "__main__":
    main()
