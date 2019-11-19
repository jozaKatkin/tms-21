# Описать функцию is_power_n( k , n ) логического типа, возвращающую
# True, если целый параметр k (> 0) является степенью числа n (> 1), и False
# в противном случае. Дано число n (> 1) и набор из 10 целых положитель-
# ных чисел. С помощью функции is_power_n найти количество степеней чис-
# ла N в данном наборе.


def is_power_n(k, n):
    while True:
        k /= n
        if k == 1:
            res = True
            break
        if k % n != 0:
            res = False
            break
    return res


def main():
    n = 2
    list_of_powers = [5, 6, 15, 8, 3, 1, 22, 97, 11, 4]
    count = 0
    for power in list_of_powers:
        if is_power_n(power, n):
            count += 1
    print(count)


if __name__ == "__main__":
    main()
