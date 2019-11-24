# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.


func = lambda some_list: [f"{i} - {string}" for i, string in enumerate(some_list)]
print(func(["hello", "world", "joe"]))
