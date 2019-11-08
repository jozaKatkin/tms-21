# Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’: ‘value’}).

# while
dict1 = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub',
}
dict_length = len(dict1)
keys_list = list(dict1.keys())
item_num = 0
while item_num < dict_length:
    old_key = keys_list[item_num]
    key_length = len(old_key)
    new_key = f'{old_key}{key_length}'
    dict1[new_key] = dict1.pop(old_key)
    item_num += 1
print(dict1)

# for
dict1 = {
    'test': 'test_value',
    'europe': 'eur',
    'dollar': 'usd',
    'ruble': 'rub',
}
keys_list = list(dict1.keys())
for old_key in keys_list:
    key_length = len(old_key)
    new_key = f'{old_key}{key_length}'
    dict1[new_key] = dict1.pop(old_key)
print(dict1)
