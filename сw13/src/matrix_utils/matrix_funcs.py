def max_elem(matrix_obj):
    max_num = matrix_obj.data[0][0]
    for row in matrix_obj.data:
        for j in row:
            if max_num < j:
                max_num = j
    return max_num


def min_elem(matrix_obj):
    min_num = matrix_obj.data[0][0]
    for row in matrix_obj.data:
        for j in row:
            if min_num > j:
                min_num = j
    return min_num


def sum_of_elements(matrix_obj):
    total = 0
    for row in matrix_obj.data:
        for elem in row:
            total += elem
    return total
