# Создать матрицу случайных чисел и сохранить ее в json файл.
# После прочесть ее, обнулить все четные элементы и сохранить в другой файл

from random import randint
import json

matrix1 = []
for i in range(5):
    line = []
    for j in range(5):
        line.append(randint(1, 9))
    matrix1.append(line)

with open('task_10_07.txt', 'w') as in_file:
    data = json.dumps(matrix1)
    in_file.write(data)

with open('task_10_07.txt') as in_file:
    data = json.loads(in_file.read())
    new_matrix = []
    for old_line in data:
        line = []
        for elem in old_line:
            line.append(0) if not elem % 2 else line.append(elem)
        new_matrix.append(line)

with open('task_10_07_01.txt', "w") as out_file:
    out_file.writelines(str(new_matrix))
