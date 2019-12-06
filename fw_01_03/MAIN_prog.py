from settings import ENGINE


engine = input("Type in json or csv")
ENGINE = ENGINE(engine)

if ENGINE is False:
    from csv_tools import (
        add_to_csv,
        del_from_csv,
        search_users,
        filter_users,
        make_correction
    )

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


if ENGINE is True:
    from json_tools import (
        input_to_dict_converter,
        create_user,
        print_dicts,
        search,
        read_json,
        filter_users,
        make_correction,
        delete_user
    )

    while True:

        func = input("Type:\n1 - to create a user\n2 - to delete a user\n3 "
                     "- to search\n4 - to filter\n5 - to correct user's data\n0 - to stop the program\n")

        if func == "1":
            answer = input("Does the file exist?\nType in yes/no\n")
            filename = input("Type here a name of the file\n")
            firstname = input("Type:\nFirst Name:\n")
            lastname = input("Last Name:\n")
            birthday = input("Birthday\n")
            profession = input("Profession\n")
            id_ = input("id:\n")
            raw_data = input_to_dict_converter(firstname, lastname, birthday, profession, id_)
            create_user(filename, raw_data, answer)
            print("User is created\n")

        elif func == "2":
            filename = input("Type here a name of the file\n")
            request = input(
                "And a user to delete:\nYou may write name, profession etc, for better accuracy type in id\n")
            delete_user(filename, request)

        elif func == "3":
            filename = input("Enter a name of the file\n")
            request = input("And your request, for example year of birth\n")
            print_dicts(search(read_json(filename), request))

        elif func == "4":
            filename = input("Enter a filename\n")
            request = input("And value to filter\n")
            print_dicts(filter_users(read_json(filename), request))

        elif func == "5":
            filename = input("Enter a filename\n")
            requested_user = input("And requested user, f. e. name, year of birth, for better accuracy type in id\n")
            key = input("Enter which key to change\n")
            new_value = input("Enter a new value\n")
            make_correction(filename, key, new_value, requested_user)

        elif func == "0":
            print("Closing the program\n")
            break

        else:
            print("Input should be a number from 0 to 6\n")
            break



