# В заданной строке расположить в обратном порядке все слова. Разделителями слов считаются пробелы.

# через срез
my_string = "hello world spam eggs ham"
my_string = my_string.split()
my_string = my_string[::-1]
print(my_string)

# через цикл
my_string = "hello world spam eggs ham"
my_string = my_string.split()
for word in reversed(my_string):
    print(word, end=" ")

# просто reversed
my_string = " ".join(reversed(my_string))
print(f"\n{my_string}")
