# Создать lambda функцию, которая принимает на вход неопределенное количество именных
# аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

func = lambda **kwargs: {kwarg[0]*2: kwarg[1] for kwarg in kwargs.items()}
print(func(abc=5, hel=1))
