# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.

m = int(input("От: "))
n = int(input("До: "))
for num in range(m, n + 1):
    divisors = []
    for divisor in range(1, num):
        if num % divisor == 0 and divisor != 1 and num != divisor:
            divisors.append(divisor)
    print(f"{num}: {divisors}")
