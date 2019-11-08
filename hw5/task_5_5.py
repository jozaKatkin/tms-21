# В массиве целых чисел с количеством элементов 19 определить
# максимальное число и заменить им все четные по значению элементы.
from random import randint

count = 0
arr = [randint(0, 30) for elem in range(19)]
print(f"Старый список: {arr}\nМаксимальное число: {max(arr)}")
for num in arr:
    if num % 2 == 0:
        arr[count] = max(arr)
    count += 1
print(f"Новый список: {arr}")
