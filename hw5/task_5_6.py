# Задан целочисленный массив. Определить количество участков массива,
# на котором элементы монотонно возрастают
# (каждое следующее число больше предыдущего)
from random import randint

my_list = [randint(0, 10) for elem in range(0, 20)]
print(my_list)
result = 0
count = 0
for i in range(len(my_list) - 1):
    if my_list[i + 1] > my_list[i]:
        count += 1
    elif my_list[i + 1] < my_list[i] and count >= 1:
        count = 0
        result += 1
print(result)
