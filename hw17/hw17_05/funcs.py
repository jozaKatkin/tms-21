import csv


def read_csv(filename):
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    return fields, rows


def prepare_csv_data(fileds, rows):
    list_fields = fileds.split(',')
    list_rows = []
    for row in rows:
        list_rows.append(row.split(','))
    return list_fields, list_rows


def print_csv(filename):
    fields, rows = read_csv(filename)
    for col in fields:
        print(col.ljust(30, " "), end='')
    print()
    for row in rows:
        for col in row:
            print(col.ljust(30, " "), end='')
        print()


def write_csv(filename, fields, rows):
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def add_row_to_csv(filename, row, position=None):
    fields, rows = read_csv(filename)

    if position is None:
        rows.append(row.split(','))
    else:
        rows.insert(position - 1, row.split(','))

    write_csv(filename, fields, rows)


def del_row_from_csv(filename, position=None):
    fields, rows = read_csv(filename)

    if position is None:
        rows.pop()
    else:
        rows.pop(position - 1)

    write_csv(filename, fields, rows)


def count_total_products_amount(filename):
    fields, rows = read_csv(filename)

    amount_index = fields.index('Amount')
    total_products_amount = 0
    for i in range(len(rows)):
        total_products_amount += int(rows[i][amount_index])
    return total_products_amount


def find_max_price_product(filename):
    fields, rows = read_csv(filename)

    price_index = fields.index('Price')
    max_price = float(rows[0][price_index])
    max_price_product_ind = 0
    for i in range(len(rows)):
        product_price = float(rows[i][price_index])
        if product_price > max_price:
            max_price = product_price
            max_price_product_ind = i

    name_index = fields.index('Product Name')
    max_price_product_name = rows[max_price_product_ind][name_index]

    return max_price_product_name, max_price


def find_min_price_product(filename):
    fields, rows = read_csv(filename)

    price_index = fields.index('Price')
    min_price = float(rows[0][price_index])
    min_price_product_ind = 0
    for i in range(len(rows)):
        product_price = float(rows[i][price_index])
        if product_price < min_price:
            min_price = product_price
            min_price_product_ind = i

    name_index = fields.index('Product Name')
    min_price_product_name = rows[min_price_product_ind][name_index]

    return min_price_product_name, min_price


def reduce_product_amount(filename, product_name, diff=1):
    fields, rows = read_csv(filename)

    name_index = fields.index('Product Name')
    amount_index = fields.index('Amount')
    for i in range(len(rows)):
        if rows[i][name_index] == product_name:
            if int(rows[i][amount_index]) < diff:
                print('Result amount could not be negative')
            else:
                rows[i][amount_index] = str(int(rows[i][amount_index]) - diff)
            break
    else:
        print(f'There is no product with name "{product_name}"')
        return
    write_csv(filename, fields, rows)