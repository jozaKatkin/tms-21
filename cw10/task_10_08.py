# Написать функции по работе с csv файлами в файле csv_utils.py. Чтение. Запись.
# Добавление записи(по позиции, по-умолчанию в конец).
# Удаление записи(по позиции, по-умолчанию последнюю).
# В файле task_10_08 импортировать функции.
# С помощью функций создать файл с информацией о товарах(Имя товара, цена, количество, комментарий).
# Прочесть файл, Добавить новую позицию в конец. Удалить третью строку.

from csv_utils import read_csv, write_csv, add_to_csv, del_from_csv, sum_of_prices

write_csv("items.csv", ["name", "price", "quantity", "commentary"],
          ["Juice", 4.1, 10, "Tomato"], ["Bun", 1, 15, "With cinnamon"],
          ["Yogurt", 2.5, 9, "Unsweetened"], ["Snickers", 2, 21, "50g"])

read_csv("items.csv")
add_to_csv("items.csv", "Water", "1.3", "17", "Mineral")
del_from_csv("items.csv", 2)
