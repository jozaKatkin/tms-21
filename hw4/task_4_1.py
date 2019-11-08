# Дан список целых чисел.
# Создать новый список, каждый элемент которого равен исходному элементу умноженному на -2

# while
list1 = input("Введите список целых чисел\n")
list1 = list1.split(" ")
final_list = []
index = 0
length = len(list1)
while index < length:
    calculation = int(list1[index]) * -2
    final_list.append(calculation)
    index += 1
print(final_list)

# for
list1 = input("Введите список целых чисел\n")
list1 = list1.split(" ")
final_list = []
for i in list1:
    calculation = int(i) * -2
    final_list.append(calculation)
print(final_list)
