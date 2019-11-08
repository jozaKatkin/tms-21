# Дан список целых чисел. Подсчитать сколько четных чисел в списке

# while
list1 = input("Введите список целых чисел\n")
list1 = list1.split(" ")
count = 0
index = 0
length = len(list1)
while index < length:
    element = int(list1[index])
    if element % 2 == 0:
        count += 1
    index += 1
print(f"Кол-во четных чисел: {count}")

# for
list1 = input("Введите список целых чисел\n")
list1 = list1.split(" ")
count = 0
for i in list1:
    if int(i) % 2 == 0:
        count += 1
print(f"Кол-во четных чисел: {count}")
