# Дан словарь, создать новый словарь, поменяв местам ключ и значение

my_dict = {
    "Kate": "k",
    "Joza": "z",
    "larisa": "1",
    "hello": "world"
}

new_dict = {value: key for key, value in my_dict.items()}
print(new_dict)