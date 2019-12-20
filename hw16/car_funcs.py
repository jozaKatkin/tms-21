from sqlalchemy.orm import sessionmaker
from brand import Brand
from car import Car
from db_connections import ENGINE
from brand_funcs import print_brands, get_brand

Session = sessionmaker(bind=ENGINE)


def get_cars():
    session = Session()
    cars = session.query(Car).all()
    session.close()
    return cars


def print_cars():
    cars = get_cars()
    for car in cars:
        print(str(car))


def enter_car():
    model = input('Model: ')
    release_year = int(input('Year: '))
    brand = input('Brand: ')
    return model, release_year, brand


def search_by_string(brand_name):
    session = Session()
    brand = session.query(Brand).filter_by(name=brand_name).first()
    session.close()
    return brand


def add_car():
    session = Session()
    model, release_year, brand_name = enter_car()
    brand = search_by_string(brand_name)
    car = Car(
        model=model,
        release_year=release_year,
        brand=brand
    )
    session.add(car)
    print(f'Car: {car} added!')
    session.commit()


def get_car(car_id):
    session = Session()
    car = session.query(Car).filter_by(id=car_id).first()
    session.close()
    return car


def choose_colon():
    print("\nChoose which colon to update: ",
          "  1. Model",
          "  2. Release year",
          "  3. Brand",
          sep="\n")
    colon = int(input("Your choice: "))
    colons = {
        1: "model",
        2: "release year",
        3: "brand"
    }
    return colons[colon]


def car_update():
    id_ = input('Enter car id: ')
    car = get_car(id_)
    colon = choose_colon()
    if colon == 'brand':
        print_brands()
        brand_id = input('Brand id: ')
        brand = get_brand(brand_id)
        car.brand = brand
    else:
        new_value = input('\nEnter new value: ')
        setattr(car, colon, new_value)
    session = Session()
    session.add(car)
    session.commit()
    print(f'Car ID:{car} successfully updated!')


def car_delete():
    session = Session()
    id_ = input("Enter id: ")
    car = get_car(id_)
    session.delete(car)
    print(f'Car {car} successfully deleted!')
    session.commit()




