# Создать матрицу случайных чисел от a до b, размерность матрицы n*m
from random import randint

m = int(input())
n = int(input())
a = int(input())
b = int(input())
my_matrix = []
print("matrix")
for i in range(m):
    line = []
    for j in range(n):
        line.append(randint(a, b))
        print("%4d" % line[j], end='')
    my_matrix.append(line)
    print()
# print(my_matrix)

# Найти максимальный элемент матрицы
max_num = my_matrix[0][0]
for row in my_matrix:
    for j in row:
        if max_num < j:
            max_num = j
print(f"Maximum number: {max_num}")

# Найти минимальный элемент матрицы
min_num = my_matrix[0][0]
for row in my_matrix:
    for j in row:
        if min_num > j:
            min_num = j
print(f"Minimum number: {min_num}")

# Найти сумму всех элементов матрицы
add = 0
for row in my_matrix:
    for i in row:
        add += i
print(f"Sum of elements in matrix: {add}")

# Найти индекс ряда с максимальной суммой элементов
max_sum = 0
index = 0
for i, row in enumerate(my_matrix):
    row_sum = 0
    for j in row:
        row_sum += j
    if max_sum < row_sum:
        max_sum = row_sum
        index = i
print(f"max sum row index: {index}")
