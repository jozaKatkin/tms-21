from sqlalchemy.orm import sessionmaker
from brand import Brand
from car import Car
from db_connections import engine


def session_starter():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def get_cars():
    session = session_starter()
    cars = session.query(Car).all()
    session.close()
    return cars


def print_cars():
    cars = get_cars()
    for car in cars:
        print("{: <2s}{:<5s}{:<5s}".format(str(car.id), str(car.model), str(car.release_year)))


def enter_car():
    model = input('Model: ')
    release_year = int(input('Year: '))
    brand = input('Brand: ')
    return model, release_year, brand


def search_by_string(brand_name):
    session = session_starter()
    brand = session.query(Brand).filter_by(name=brand_name).first()
    session.close()
    return brand


def add_car():
    session = session_starter()
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
    session = session_starter()
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
    id_ = input('Enter id: ')
    car = get_car(id_)
    colon = choose_colon()
    new_value = input("\nEnter new value: ")
    setattr(car, colon, new_value)
    session = session_starter()
    session.add(car)
    print(f'Car: {car} successfully updated!')
    session.commit()


def car_delete():
    session = session_starter()
    id_ = input("Enter id: ")
    car = get_car(id_)
    session.delete(car)
    print(f'Car {car} successfully deleted!')
    session.commit()




