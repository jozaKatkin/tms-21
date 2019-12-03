from prog_tools import (
    write_json,
    read_json,
    create_user,
    filter_users,
    print_dicts,
    make_correction,
    search,
    delete_user
)

DEBUG = True
if DEBUG == True:
    func = "1"
    filename = "users2.json"
    data = {"First Name": "Petr", "LastName": "Pchyolkin", "Birthday": "01.01.1960", "Profession": "Security","id": "0010"}, {"First Name": "Masha", "LastName": "Kot", "Birthday": "02.02.2006", "Profession": "School", "id": "0020"}


while True:

    func = input("Type:\n1 - to write a file\n2 -  to create a user\n3 - to delete a user\n4 "
                 "- to search\n5 - to filter\n6 - to correct user's data\n0 - to stop the program\n")
    # if func != "1" or "2" or "3" or "4" or "5" or "6" or "0":
    #     print("Input should be a number from 0 to 6")
    #     continue
    if func == "1":
        filename = input("Type here a name of the file\n")
        data = input("And data to be written (list of dictionaries)\n")
        # if not isinstance(data, list):
        #     print("\nInput should be a list\n")
        #     print(type(data))
        #     print(data)
        #     break
        # for elem in data:
        #     if not isinstance(elem, dict):
        #         print("Data in a list should be wrapped in dictionaries\n")
        #         break
        # else:
        write_json(filename, data)
        print(type(data))
        print("File is written\n")
        break

    elif func == "2":
        filename = input("Type here a name of the file\n")
        data = input("And a user to be written\n")
        if not isinstance(data, dict):
            print("User should be wrapped in a dictionary\n")
            break
        else:
            create_user(filename, data)
            print("User is created\n")

    elif func == "3":
        filename = input("Type here a name of the file")
        request = input("And a user to delete\nYou may write name, profession etc, but for better accuracy type in id\n")
        delete_user(filename, request)
        print("User is deleted\n")

    elif func == "4":
        filename = input("Enter a name of the file\n")
        request = input("And your request, for example year of birth\n")
        print_dicts(search(read_json(filename), request))

    elif func == "5":
        filename = input("Enter a filename\n")
        request = input("And your request\n")
        print_dicts(filter_users(read_json(filename), request))

    elif func == "6":
        filename = input("Enter a filename\n")
        requested_user = input("And requested user, f. e. name, year of birth, but for better accuracy type in id\n")
        key = input("Enter which key to change\n")
        new_value = input("Enter a new value to be changed\n")
        make_correction(filename, key, new_value, requested_user )
        print("Correction is made")

    elif func == "0":
        print("Closing the program\n")
        break

    else:
        print("Input should be a number from 0 to 6\n")
        break


