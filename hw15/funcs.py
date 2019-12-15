from classes import Product, engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from exceptions import (
    WrongColonError,
    WrongIdError,
    WrongValueError
)


def read_table():
    e = create_engine("sqlite:///database0.db")
    result = e.execute("""select * from products""")
    return result


def print_table(enter):
    rows = read_table()
    for row in rows:
        for col in row:
            print("{:_^15s} ".format(str(col)), sep='', end='')
        print()


def get_product_id(id_):
    Session = sessionmaker(bind=engine)
    session = Session()
    product = session.query(Product).get(id_)
    return product, session


def print_by_id(id_):
    product, session = get_product_id(id_)
    if product is None:
        raise WrongIdError
    session.commit()
    print(product)


def add_product(args):
    name, price, amount = args.split(", ")
    Session = sessionmaker(bind=engine)
    session = Session()
    id_ = "defined"
    product = Product(id_, name, price, amount)
    try:
        product.amount = int(amount)
    except ValueError:
        raise WrongValueError
    session.add(product)
    session.commit()
    print(product)


def update_product(args):
    id_, colon_name, new_value = args.split(", ")
    if colon_name == "name" or colon_name == "price" or colon_name == "amount":
        product, session = get_product_id(id_)
        if colon_name == "name":
            product.name = new_value
        elif colon_name == "price":
            product.price = new_value
        elif colon_name == "amount":
            try:
                product.amount = int(new_value)
            except ValueError:
                raise WrongValueError
        session.add(product)
        session.commit()
        print(product)
    else:
        raise WrongColonError


def delete_product(id_):
    product, session = get_product_id(id_)
    if product is None:
        raise WrongIdError
    session.delete(product)
    session.commit()



