from brand_funcs import (
    add_brand,
    brand_update,
    brand_delete,
    print_brands,
)
from car_funcs import (
    add_car,
    car_update,
    car_delete,
    print_cars,
)

BRAND = 1
CAR = 2

CONFIG = {
    BRAND: {
        1: add_brand,
        2: brand_update,
        3: brand_delete,
        4: print_brands,
    },
    CAR: {
        1: add_car,
        2: car_update,
        3: car_delete,
        4: print_cars,

    },
}
