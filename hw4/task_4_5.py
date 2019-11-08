# Составить список чисел Фибоначчи содержащий 15 элементов.

# while
num1 = num2 = 1
i = 1
new_list = [num1, num2]
while i < len(new_list):
    sum1 = num1 + num2
    num1 = num2
    num2 = sum1
    new_list.append(num2)
    i += 1
    if len(new_list) == 15:
        break
print(new_list)

# for
num1 = num2 = 1
new_list = [num1, num2]
for i in range(13):
    sum1 = num1 + num2
    num1 = num2
    num2 = sum1
    new_list.append(num2)
print(new_list)
