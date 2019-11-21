# Создать lambda функцию, которая принимает на вход список имен и выводит
# их в формате “Hello, {name}” в другой список

func = lambda names: [f"Hello, {name}" for name in names]
print(func(["Ekaterina", "Joza", "Oleg"]))