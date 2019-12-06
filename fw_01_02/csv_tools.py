import csv


def read_csv(filename):
    """Reading"""
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return fields, rows


def converter(fields, rows):
    """Converting data for writing to csv"""
    list_fields = fields.split(',')
    list_rows = []
    for row in rows:
        list_rows.append(row.split(','))
    return list_fields, list_rows


def print_csv(filename):
    """Printing"""
    fields, rows = read_csv(filename)
    for col in fields:
        print("{:_^15s} ".format(col), end='')
    print()
    for row in rows[:5]:
        for col in row:
            print("{:_^15s} ".format(col), sep='', end='')
        print()


def write_csv(filename, fields, rows):
    """Writing"""
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def write_row_to_csv(filename, row):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)


def add_to_csv(filename, row, answer):
    """Adding user to csv"""
    if answer == "yes":
        fields, rows = read_csv(filename)
        rows.append(row.split(","))
        write_csv(filename, fields, rows)
    elif answer == "no":
        write_row_to_csv(filename, row.split(","))
    else:
        print("Invalid input\nType in yes/no\n")


def del_from_csv(filename, request):
    """Deletion"""
    fields, rows = read_csv(filename)
    user = filter_users(filename, request)
    if len(user) > 1:
        print("Multiple users found upon your request, type in id for better accuracy")
    elif len(user) < 1:
        pass
    else:
        print(user[0])
        user = user[0]
        rows.remove(user)
        write_csv(filename, fields, rows)
        print("User is deleted")


def filter_users(filename, request):
    """Filter users upon request, returns users if the whole value in user found"""
    list_of_users = []
    fields, rows = read_csv(filename)
    if len(rows) == 0:
        print("No rows found\n")
    else:
        for row in rows:
            if request in row and row not in list_of_users:
                list_of_users.append(row)
        if len(list_of_users) == 0:
            print("No users found upon your request\n")
    return list_of_users


def search_users(filename, request):
    """Search users upon request, returns user if part of the value found in user"""
    list_of_users = []
    fields, rows = read_csv(filename)
    if len(rows) == 0:
        print("No rows found\n")
    else:
        for row in rows:
            for elem in row:
                if request in elem and row not in list_of_users:
                    list_of_users.append(row)
        if len(list_of_users) == 0:
            print("No users found upon your request\n")
    return list_of_users


def make_correction(filename, colon_in_field, new_value, requested_user):
    """Correct value in user"""
    user = filter_users(filename, requested_user)
    fields, rows = read_csv(filename)
    if len(rows) == 0:
        print("No rows found\n")
    elif len(user) < 1:
        pass
    elif len(user) > 1:
        print("Too much users found, type in id for better accuracy\n")
        for user in user:
            print(user)
    else:
        print(user[0])
        request_index = fields.index(colon_in_field)
        user_index = rows.index(user[0])
        rows[user_index][request_index] = new_value
        print(rows[user_index])
        write_csv(filename, fields, rows)
