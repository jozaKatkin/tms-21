import json


def write_json(filename, data):
    with open(filename, 'w') as my_file:
        data = json.dumps(data, indent=4)
        my_file.write(data)


def read_json(filename):
    with open(filename) as my_file:
        data = json.loads(my_file.read())
        return data


# def print_json(filename):
#     with open(filename):
#         for user in read_json(filename):
#             user = user.items()
#             for key, value in user:
#                 print(f"{key}: {value}")
#             print()


def print_dicts(data):
    """Pass here a finished list of dictionaries"""
    for user in data:
        for key, value in user.items():
            print(f"{key}: {value}")
        print()


def create_user(filename, raw_data, answer):
    answer = answer.lower()
    if answer == "yes":
        data = read_json(filename)
        if len(data) == 0:
            print("File was empty")
            write_json(filename, [raw_data])
        else:
            data.append(raw_data)
            write_json(filename, data)
    elif answer == "no":
        print("Creating a new file...")
        write_json(filename, [raw_data])
    else:
        print("Invalid input\nType in yes/no\n")


def make_correction(filename, key, new_value, requested_user):
    while True:
        data = read_json(filename)
        user = search(data, requested_user)
        if len(data) == 0:
            break
        elif len(user) > 1:
            print("Too much users found, type in id for better accuracy\n")
            print_dicts(user)
        elif len(user) < 1:
            break
        else:
            print_dicts(user)
            user = user[0]
            user[key] = new_value
            print(user)
            write_json(filename, data)
        break


def filter_users(data, request):
    list_of_users = []
    if len(data) == 0:
        print("File is empty")
    else:
        for user in data:
            if request in user.values():
                list_of_users.append(user)
        if len(list_of_users) == 0:
            print("No users found upon your request")
    return list_of_users


def search(data, request):
    list_of_users = []
    if len(data) == 0:
        print("File is empty")
    else:
        for user in data:
            for value in user.values():
                if request in value and user not in list_of_users:
                    list_of_users.append(user)
        if len(list_of_users) == 0:
            print("No users found upon your request")
    return list_of_users


def delete_user(filename, request):
    data = read_json(filename)
    user = search(data, request)
    if len(user) > 1:
        print("Multiple users found upon your request, type in id for better accuracy")
    elif len(user) < 1:
        pass
    else:
        print_dicts(user)
        user = user[0]
        data.remove(user)
        write_json(filename, data)
        print("User is deleted")


def input_to_dict_converter(firstname, lastname, birthday, profession, id_):
    user_dict = {
        "First Name": firstname,
        "Last Name": lastname,
        "Birthday": birthday,
        "Profession": profession,
        "id": id_
    }
    return user_dict
