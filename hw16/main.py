from ui import ui
from hw16.db_connections import Base, ENGINE

Base.metadata.create_all(ENGINE)


def main():
    ui()


if __name__ == '__main__':
    main()