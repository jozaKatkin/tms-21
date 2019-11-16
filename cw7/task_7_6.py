def my_func(*args):
    add = 0
    max_num = args[0]
    for num in args:
        add += num
        if max_num < num:
            max_num = num

    return add, max_num


print(my_func(6, 7, 8, 9))
