# Дана целочисленная квадратная матрица. Найти в каждой строке наибольший
# элемент и поменять его местами с элементом главной диагонали.

from random import randint

n = int(input("Введите размерность квадратной матрицы: "))
matrix1 = []
print("old matrix:")
for i in range(n):
    line = []
    for j in range(n):
        line.append(randint(1, 10))
    matrix1.append(line)
    print(line)
print("new matrix:")
count = 0
for line in matrix1:
    for elem in line:
        index = line.index(max(line))
        line[count], line[index] = line[index], line[count]
    count += 1
    print(line)
