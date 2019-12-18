from sqlalchemy.orm import sessionmaker
from album import Album
from artist import Artist
from db_connection import Base, engine


def main():
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    artist = Artist(name='MyBand')
    album = Album(name='MyAlbum', artist=artist)
    session.add_all([artist, album])
    session.commit()


if __name__ == '__main__':
    main()
