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
    for i, user in enumerate(data):
        for key, value in user.items():
            print(f"{key}: {value}")
        print()


def create_user(filename, raw_data):
    data = read_json(filename)
    data.append(raw_data)
    write_json(filename, data)


def make_correction(filename, key, new_value, requested_user):
    data = read_json(filename)
    user = filter_users(data, requested_user)
    if len(user) != 1:
        print("Too much users or no such a user\n")
    user = user[0]
    user[key] = new_value
    write_json(filename, data)


def filter_users(data, request):
    list_of_users = []
    for user in data:
        if request in user.values():
            list_of_users.append(user)
    return list_of_users




