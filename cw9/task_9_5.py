# Дан список чисел. Найти произведение всех чисел, которые кратны 3

from functools import reduce


def main():
    result = reduce(lambda a, num: a * num, filter(lambda num: num % 3 == 0, [1, 2, 3, 6, 4]), 1)
    print(result)


if __name__ == "__main__":
    main()
