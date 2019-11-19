# Дан список чисел. Посчитать сколько раз встречается каждое число. Использовать функцию.
# Подсказка: для хранения данных использовать словарь. Для проверки нахождения элемента
# в словаре использовать метод get(), либо оператор in


def calc_repeat(numbers):
    new_dict = {}
    for num in numbers:
        if num in new_dict:
            new_dict[num] += 1
        else:
            new_dict[num] = 1

    print(new_dict)
    return new_dict


def main():
    calc_repeat([1, 2, 1, 3, 3, 3, 0])


if __name__ == "__main__":
    main()
