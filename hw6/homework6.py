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
