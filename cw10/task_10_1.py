# Имеется текстовый файл. Напечатать:

# a) его первую строку;
my_file = open('test.txt')
print(f"1 line: {my_file.readline()}")
my_file.close()

# b) его пятую строку;
my_file = open('test.txt')
print(f"5th line: {my_file.readlines()[4:5]}\n")
my_file.close()

# c) его первые 5 строк;
my_file = open('test.txt')
print(f"first 5 lines: {my_file.readlines()[:5]}\n")
my_file.close()

# d) его строки с s1-й по s2-ю;
my_file = open('test.txt')
print(f"1-2 lines: {my_file.readlines()[0:2]}\n")
my_file.close()

# e) весь файл
my_file = open('test.txt')
print(f"The whole file: {my_file.readlines()}")
my_file.close()
