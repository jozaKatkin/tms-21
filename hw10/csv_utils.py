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
    list_fields = fields.split(",")
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


def add_to_csv(filename, row, position=None):
    """Addition"""
    fields, rows = read_csv(filename)
    if position is None:
        rows.append(row.split(","))
    else:
        rows.insert(position - 1, row.split(","))
    write_csv(filename, fields, rows)


def del_from_csv(filename, position=None):
    """Deletion"""
    fields, rows = read_csv(filename)
    if position is None:
        rows.pop()
    else:
        rows.pop(position - 1)
    write_csv(filename, fields, rows)


def sum_of_items(filename, colon):
    """Count sum of all the items"""
    fields, rows = read_csv(filename)
    colon_index = fields.index(colon)
    items_sum = 0
    for i, row in enumerate(rows):
        items_sum += int(rows[i][colon_index])
    return items_sum


def most_expensive(filename, colon):
    """Find the most expensive item"""
    fields, rows = read_csv(filename)
    max_price = 0.0
    colon_index = fields.index(colon)
    for i, row in enumerate(rows):
        product_price = float(rows[i][colon_index])
        if product_price > max_price:
            max_price = product_price
            max_prod_index = i
    index_name = fields.index("name")
    name = rows[max_prod_index][index_name]
    return name, max_price


def cheapest(filename, colon):
    """Find the cheapest item"""
    fields, rows = read_csv(filename)
    colon_index = fields.index(colon)
    min_price = float(rows[0][colon_index])
    for i, row in enumerate(rows):
        product_price = float(rows[i][colon_index])
        if product_price < min_price:
            min_price = product_price
            min_prod_index = i
    index_name = fields.index("name")
    name = rows[min_prod_index][index_name]
    return name, min_price


def reduce_quantity(filename, product_name, quantity=1):
    """Reduce quantity of an item in selected position"""
    fields, rows = read_csv(filename)
    name_index = fields.index("name")
    quantity_index = fields.index("quantity")
    for i, row in enumerate(rows):
        if rows[i][name_index] == product_name:
            if int(rows[i][quantity_index]) < quantity:
                print("Bad guy!")
            else:
                rows[i][quantity_index] = str(int(rows[i][quantity_index]) - quantity)
            break

    else:
        print(f"Mistake")
        return
    write_csv(filename, fields, rows)