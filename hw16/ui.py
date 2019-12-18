from config import (
    CONFIG,
)


def ui():
    while True:
        print("Choose:",
              "  1. Brand",
              "  2. Car",
              "  0. Exit",
              sep="\n")
        table_type = int(input("Input your choice: "))
        if not table_type:
            break
        print("Choose action:",
              "  1. Add item",
              "  2. Update item",
              "  3. Delete item",
              "  4. Read Table",
              "  0. Exit",
              sep="\n")
        action = int(input("Input your choice: "))
        if not action:
            break
        func = CONFIG[table_type].get(action)
        func()
        input("Press ENTER to continue\n")
