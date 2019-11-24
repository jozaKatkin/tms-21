# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных
# удалять все четные элементы из списка


def del_odd_decorator(func):
    def del_odd(*args):
        args_list = list(args)
        new_list = []
        [new_list.append(num) for num in args_list if num % 2 != 0]
        return new_list

    return del_odd


@del_odd_decorator
def nums(*args):
    nums_list = list(args)
    return nums_list


print(nums(1, 5, 3, 2, 8, 6, 9, 7, 12))
