# Описать функцию fact2( n ) вещественного типа, вычисляющую двойной факториал:
# n!! = 1·3·5·...·n, если n — нечетное; n!! = 2·4·6·...·n, если n — четное
# (n > 0 — параметр целого типа. С помощью этой функции найти двойные факториалы пяти данных целых чисел


def fact2(n):
    fact = 1
    if not n % 2:  # even
        for num in range(2, n + 1, 2):
            fact *= num
    if n % 2 != 0:  # odd
        for num in range(1, n + 1, 2):
            fact *= num

    return fact


def main():
    nums = [3, 5, 4, 9, 6]
    print([fact2(num) for num in nums])


if __name__ == "__main__":
    main()
