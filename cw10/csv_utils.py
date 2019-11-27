import csv


def read_csv(filename):
    """Reading"""
    rows = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        print("Total no. of rows: %d" % (csvreader.line_num))
    for col in fields:
        print("%15s" % col, end='')
    print()
    for row in rows[:5]:
        for col in row:
            print("%15s" % col, sep='', end='')
        print()


def write_csv(filename, fields, *rows):
    """Writing"""
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)


def add_to_csv(filename, *args, position=-1):
    """Addition"""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        args = ",".join(args)
        args = args.split(",")
        new_list = []
        for line in csvreader:
            new_list.append(line)
        if position == -1:
            new_list.append(args)
        else:
            new_list.insert(position, args)
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_list)


def del_from_csv(filename, position=-1):
    """Deletion"""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # args = ",".join(args)
        # args = args.split(",")
        new_list = []
        for line in csvreader:
            new_list.append(line)
        del new_list[position]
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_list)


def sum_of_prices(filename):
    """Count sum of prices for all the items"""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        items_sum = 0
        for i, row in enumerate(csvreader):
            if i == 0:
                continue
            items_sum += float(row[1])
        return items_sum


def most_expensive(filename):
    """Find the most expensive item"""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        max_price = 0
        for i, row in enumerate(csvreader):
            if i == 0:
                pass
            elif float(row[1]) > max_price:
                max_price = float(row[1])
                res = row[0]
        return res, max_price


def cheapest(filename):
    """Find the cheapest item"""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        min_price = None
        for i, row in enumerate(csvreader):
            if i == 0:
                pass
            elif min_price is None or float(row[1]) < min_price:
                min_price = float(row[1])
                res = row[0]
        return res, min_price


def reduce_quantity(filename, position, quantity=1):
    """Reduce quantity of an item in selected position"""
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        new_list = []
        for i, row in enumerate(csvreader):
            new_list.append(row)
            if i == position:
                row[2] = int(float(row[2]) - float(quantity))
                res = f"{row[0]}, {row[2] + quantity} --> {row[2]}"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(new_list)
    return res



