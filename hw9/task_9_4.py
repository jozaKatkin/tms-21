# Создать универсальны декоратор, который меняет порядок аргументов в функции на противоположный


def reorder_decorator(func):
    def wrapper(*args, **kwargs):
        args = list(args)[::-1]
        kwargs = dict(list(kwargs.items())[::-1])
        args, kwargs = kwargs, args
        return args, kwargs

    return wrapper


@reorder_decorator
def my_func(*args, **kwargs):
    print(args, kwargs)
    return args, kwargs


print(my_func(1, 2, 3, "d", "g", "h", hello="world", spam=1))
