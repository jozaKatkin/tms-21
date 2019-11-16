def factorial(num):
    start = 1
    for i in range(1, num + 1):
        fact = start * i
        start = fact
    return start


print(factorial(5))
print(factorial(1))
