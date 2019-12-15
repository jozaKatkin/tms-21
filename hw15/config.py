from funcs import (
    add_product,
    update_product,
    delete_product,
    print_by_id,
    print_table,
)

EXIT = 0
ADD = 1
UPDATE = 2
DELETE = 3
PRINT_BY_ID = 4
PRINT_TABLE = 5

CONFIG = {
    "functions": {
        EXIT: {
            "choice_message": f"{EXIT} - Close program",
        },
        ADD: {
            "function": add_product,
            "choice_message": f"{ADD} - Add product to table",
            "input_message":
            "Enter name, price, amount:\n",
        },
        UPDATE: {
            "function": update_product,
            "choice_message": f"{UPDATE} - Change value in product",
            "input_message":
            "Enter id, colon_name, new_value:\n",
        },
        DELETE: {
            "function": delete_product,
            "choice_message": f"{DELETE} - Delete product by id",
            "input_message":
            "Enter id:\n"
        },
        PRINT_BY_ID: {
            "function": print_by_id,
            "choice_message": f"{PRINT_BY_ID} - Print product by id",
            "input_message":
            "Enter id:\n",
        },
        PRINT_TABLE: {
            "function": print_table,
            "choice_message": f"{PRINT_TABLE} - Print table",
            "input_message":
            "Press ENTER to print table",
        },
    },
    "available_functions": [
        EXIT,
        ADD,
        UPDATE,
        DELETE,
        PRINT_BY_ID,
        PRINT_TABLE,
    ],
}
