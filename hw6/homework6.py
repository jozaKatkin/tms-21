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

# Найти индекс колонки с минимальной суммой элементов
min_sum = 0
colon = 0
for i in range(n):
    colon_sum = 0
    for j in range(m):
        colon_sum += my_matrix[j][i]
    if colon_sum < min_sum:
        min_sum = colon_sum
        colon = i
print(f"min sum colon index: {colon}")

# Обнулить все элементы выше главной диагонали
print("old matrix:")
for i in range(m):
    for j in range(n):
        print("%4d" % my_matrix[i][j], end='')
    print()
for i in range(m):
    for j in range(n):
        if i < j:
            my_matrix[i][j] = 0
print("new matrix:")
for i in range(m):
    for j in range(n):
        print("%4d" % my_matrix[i][j], end='')
    print()

# Обнулить все элементы ниже главной диагонали
print("old matrix:")
for i in range(m):
    for j in range(n):
        print("%4d" % my_matrix[i][j], end='')
    print()
# print(my_matrix)
for i in range(m):
    for j in range(n):
        if i > j:
            my_matrix[i][j] = 0
print("new matrix:")
for i in range(m):
    for j in range(n):
        print("%4d" % my_matrix[i][j], end='')
    print()

# Создать две новые матрицы matrix_a, matrix_b случайных чисел размерностью n*m
m = int(input())
n = int(input())
matrix_a = []
print("matrix_a:")
for i in range(m):
    line = []
    for j in range(n):
        line.append(randint(-10, 10))
        print("%4d" % line[j], end='')
    matrix_a.append(line)
    print()
# print(matrix_a)
matrix_b = []
print("matrix_b:")
for i in range(m):
    line = []
    for j in range(n):
        line.append(randint(-10, 10))
        print("%4d" % line[j], end='')
    matrix_b.append(line)
    print()
# print(matrix_b)

# Создать матрицу равную сумме matrix_a и matrix_b
sum_matrix = []
print("sum of matrix_a and matrix_b:")
for i in range(m):
    row = []
    for j in range(n):
        sum_elem = matrix_a[i][j] + matrix_b[i][j]
        row.append(sum_elem)
        print("%4d" % row[j], end='')
    sum_matrix.append(row)
    print()