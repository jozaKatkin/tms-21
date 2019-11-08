# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300.

for num in range(200, 301):
    sum_of_divisors = 0
    for divisor in range(1, num):
        if num % divisor == 0 and num != divisor:
            sum_of_divisors += divisor
    new_sum_of_divs = 0
    for n_divisor in range(1, sum_of_divisors):
        if sum_of_divisors % n_divisor == 0 and sum_of_divisors != n_divisor:
            new_sum_of_divs += n_divisor
    if num == new_sum_of_divs:
        print(num, sum_of_divisors)
