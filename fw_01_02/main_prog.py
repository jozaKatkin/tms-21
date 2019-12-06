from csv_tools import *


while True:

    func = input("Type:\n1 - to create a user\n2 - to delete a user\n3 "
                 "- to search\n4 - to filter\n5 - to correct user's data\n0 - to stop the program\n")

    if func == "1":
        answer = input("Does the file exist?\nType in yes/no\n")
        filename = input("Type here a name of the file\n")
        if answer == "yes":
            print("File shouldn't be empty!")
        if answer == "no":
            print("There are no fields, so enter them first")
        row = input("Input row to be written divided by comas, without spaces\n")
        add_to_csv(filename, row, answer)
        print("User is created\n")

    elif func == "2":
        filename = input("Type here a name of the file\n")
        request = input(
            "And a user to delete:\nYou may write name, profession etc, but for better accuracy type in id\n")
        del_from_csv(filename, request)

    elif func == "3":
        filename = input("Enter a name of the file\n")
        request = input("And your request, for example year of birth\n")
        for user in search_users(filename, request):
            print(user)

    elif func == "4":
        filename = input("Enter a filename\n")
        request = input("And value to filter\n")
        for user in filter_users(filename, request):
            print(user)

    elif func == "5":
        filename = input("Enter a filename\n")
        requested_user = input("And requested user, f. e. name, year of birth, but for better accuracy type in id\n")
        colon = input("Enter which colon to change\n")
        new_value = input("Enter a new value\n")
        make_correction(filename, colon, new_value, requested_user)

    elif func == "0":
        print("Closing the program\n")
        break

    else:
        print("Input should be a number from 0 to 6\n")
        break
