from random import randint


def m_creation(m, n, a, b):
    my_matrix = []
    for i in range(m):
        line = []
        for j in range(n):
            line.append(randint(a, b))
        my_matrix.append(line)
    return my_matrix


matrix_result = m_creation(4, 4, 0, 10)


def m_print(something):
    print(something)


m_print(matrix_result)


def addition(some_matrix):
    add = 0
    for row in some_matrix:
        for i in row:
            add += i
    return add


print(f"sum: {addition(matrix_result)}")


def max_elem(some_matrix):
    max_num = some_matrix[0][0]
    for row in some_matrix:
        for j in row:
            if max_num < j:
                max_num = j
    return max_num


print(f"max_elem: {max_elem(matrix_result)}")


def min_elem(some_matrix):
    min_num = some_matrix[0][0]
    for row in some_matrix:
        for j in row:
            if min_num > j:
                min_num = j
    return min_num


print(f"min elem: {min_elem(matrix_result)}")