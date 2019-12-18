from ui import ui
from hw16.db_connections import Base, engine

Base.metadata.create_all(engine)


def main():
    ui()


if __name__ == '__main__':
    main()