# Дано число. Найти сумму и произведение его цифр.

user_num = input("Введите число ")
sum1 = 0
multiplication = 1
for char in user_num:
    sum1 += int(char)
    multiplication *= int(char)
print(f"Сумма: {sum1}, произведение: {multiplication}")
