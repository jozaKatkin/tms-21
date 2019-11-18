list_a = ["hello", "world", "spam"]
list_a = [list_a[::-1] for i in range(1)]
print(list_a)


list_b = ["hello", "world", "spam"]
list_a = [i[::-1] for i in list_b]
print(list_a)

