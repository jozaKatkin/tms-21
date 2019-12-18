from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'Car - Brand'
DB_ECHO = True

engine = create_engine(
    # "postgresql://postgres:postgres@localhost/test",
    f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
    echo=DB_ECHO,
)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
