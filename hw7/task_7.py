# Написать 12 функций по переводу:

# 1 Дюймы в сантиметры
def inches_to_cm(inches):
    cm = inches * 2.54
    return cm


# 2 Сантиметры в дюймы
def cm_to_inches(cm):
    inches = cm / 2.54
    return inches


# 3 Мили в километры
def miles_to_km(miles):
    km = miles * 1.609
    return km


# 4 Километры в мили
def km_to_miles(km):
    miles = km / 1.609
    return miles


# 5 Фунты в килограммы
def pounds_to_kilos(pounds):
    kilos = pounds / 2.205
    return kilos


# 6 Килограммы в фунты
def kilos_to_pounds(kilos):
    pounds = kilos * 2.205
    return pounds


# 7 Унции в граммы
def ounces_to_grams(ounces):
    grams = ounces * 28.35
    return grams


# 8 Граммы в унции
def grams_to_ounces(grams):
    ounces = grams / 28.35
    return ounces


# 9 Галлон в литры
def gallons_to_litres(gallons):
    litres = gallons * 4.546
    return litres


# 10 Литры в галлоны
def litres_to_gallons(litres):
    gallons = litres / 4.546
    return gallons


# 11 Пинты в литры
def pints_to_litres(pints):
    litres = pints / 1.76
    return litres


# 12 Литры в пинты
def litres_to_pints(litres):
    pints = litres * 1.76
    return pints


# Написать программу, со следующим интерфейсом: пользователю предоставляется
# на выбор 12 вариантов перевода(описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати. После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат.
# Использовать функции из первого задания. Программа должна быть в бесконечном цикле. Код выхода из программы - “0”

while True:
    num = input("Enter number: ")
    if num == "0":
        print("The end")
        break
    value = int(input("Enter value: "))
    if num == "1":
        res = inches_to_cm(value)
    elif num == "2":
        res = cm_to_inches(value)
    elif num == "3":
        res = miles_to_km(value)
    elif num == "4":
        res = km_to_miles(value)
    elif num == "5":
        res = pounds_to_kilos(value)
    elif num == "6":
        res = kilos_to_pounds(value)
    elif num == "7":
        res = ounces_to_grams(value)
    elif num == "8":
        res = grams_to_ounces(value)
    elif num == "9":
        res = gallons_to_litres(value)
    elif num == "10":
        res = litres_to_gallons(value)
    elif num == "11":
        res = pints_to_litres(value)
    elif num == "12":
        res = litres_to_pints(value)
    print(res)
