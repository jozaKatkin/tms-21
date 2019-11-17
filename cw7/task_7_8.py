# Написать функцию принимающая на вход неопределенным количеством аргументов и именованный аргумент mean_type.
# В зависимости от mean_type вернуть среднеарифметическое либо среднегеометрическое.
# Написать программу в виде трех функций


def count_mean(*args, mean_type):
    if mean_type == "arithmetical":
        def arithmetical(some_args):
            add = 0
            for arg in some_args:
                add += arg
            arithm_mean = add / (len(some_args))
            return arithm_mean

        res = arithmetical(args)
    elif mean_type == "geometrical":
        def geometrical(some_args):
            multi = 1
            for arg in some_args:
                multi *= arg
            geom_mean = multi ** (1 / len(some_args))
            return geom_mean

        res = geometrical(args)

    return res


print(count_mean(1, 2, 3, 4, mean_type="arithmetical"))
print(count_mean(1, 2, 3, 4, mean_type="geometrical"))
