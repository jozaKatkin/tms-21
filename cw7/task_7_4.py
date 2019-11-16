from random import randint


def matrix_cr(m, n, random_from=0, random_to=9):
    my_matrix = []
    for i in range(m):
        line = []
        for j in range(n):
            line.append(randint(random_from, random_to))
        my_matrix.append(line)
    return my_matrix


result = matrix_cr(3, 3)

print(result)
