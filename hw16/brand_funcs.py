from sqlalchemy.orm import Session, sessionmaker

from brand import Brand
from db_connections import engine


def session_starter():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_brands():
    session = session_starter()
    brands = session.query(Brand).all()
    session.close()
    return brands


def print_brands():
    brands = get_brands()
    for brand in brands:
        print("{: <2s}{:<s}".format(str(brand.id), str(brand.name)))


def enter_brand():
    name = input('Enter new brand name: ')
    return name


def add_brand():
    session = session_starter()
    name = enter_brand()
    brand = Brand(
        name=name
    )
    session.add(brand)
    print(f'{brand} added!')
    session.commit()


def get_brand(brand_id):
    session = session_starter()
    brand = session.query(Brand).filter_by(id=brand_id).first()
    session.close()
    return brand


def brand_update():
    session = session_starter()
    id_ = input('Enter id: ')
    brand = get_brand(id_)
    new_value = enter_brand()
    setattr(brand, "name", new_value)
    session.add(brand)
    print(f'{brand} updated!')
    session.commit()


def brand_delete():
    session = session_starter()
    id_ = input("Enter id: ")
    brand = get_brand(id_)
    session.delete(brand)
    print(f'{brand} deleted!')
    session.commit()

