def multiplication(*args):
    sum = 0
    for num, index in enumerate(args):
        multi = num * index
        sum += multi

    return sum


print(multiplication(4, 3, 2, 1))
