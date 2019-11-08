guests = int(input("Enter a number of guests\n"))
if 20 <= guests <= 50:
    print("кафе")
elif guests < 20:
    print("дом")
else:
    print("ресторан")
