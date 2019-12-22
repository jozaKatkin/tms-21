def matrix_max_elem(matrix):
    max_elem = matrix.data[0][0]
    for i, row in enumerate(matrix.data):
        for j, elem in enumerate(row):
            if elem > max_elem:
                max_elem = elem
    return max_elem


def matrix_min_elem(matrix):
    min_elem = matrix.data[0][0]
    for i, row in enumerate(matrix.data):
        for j, elem in enumerate(row):
            if elem < min_elem:
                min_elem = elem
    return min_elem


def matrix_sum(matrix):
    summ = 0
    for line in matrix.data:
        for elem in line:
            summ += elem
    return summ