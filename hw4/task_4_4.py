# Дан список. Создать новый список, сдвинутый на 1 элемент влево
# Пример: 1 2 3 4 5 ->  2 3 4 5 1

# while
list1 = input("Введите список\n")
list1 = list1.split(" ")
new_list = []
index = 1
length = len(list1)
while index < length:
    new_list.append(list1[index])
    index += 1
new_list.append(list1[0])
print(new_list)

# for
list1 = input("Введите список\n")
list1 = list1.split(" ")
new_list = []
length = len(list1)
for num in range(1, length):
    new_list.append(list1[num])
new_list.append(list1[0])
print(new_list)
