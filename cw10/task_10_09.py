# Использовать результаты 10.8. Все функции описываются в csv_utils.py.
# Проверка работы функции осуществляется в task_10_09.py.
# Создать функцию подсчета полной суммы всех товаров.
# Создать функцию поиска самого дорогого товара.
# Создать функцию самого дешевого товара.
# Создать функцию уменьшения количества товара(на n, по-умолчанию на 1)

from csv_utils import sum_of_items, most_expensive, cheapest, reduce_quantity


def main():
    print(sum_of_items("items.csv", "quantity"))
    print(most_expensive("items.csv", "price"))
    print(cheapest("items.csv", "price"))
    reduce_quantity("items.csv", "Bun", 3)


if __name__ == "__main__":
    main()
