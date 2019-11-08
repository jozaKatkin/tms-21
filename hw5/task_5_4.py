# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число.

addition = 1
N = int(input("Введите число: "))
for i in range(2, N + 1):
    division = 1 / i
    addition += division
print(addition)
