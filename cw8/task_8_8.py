# Дан массив целых чисел A. Найти суммы положительных и отрицательных
# элементов массива, используя функцию определения суммы


def main():
    A = [1, -2, 5, 7, -1, -3, 19, 5, -4, -17]
    positive = sum(num for num in A if num > 0)
    negative = sum(num for num in A if num < 0)
    print(f"sum of positive numbers: {positive}, sum of negative numbers: {negative}")


if __name__ == "__main__":
    main()
