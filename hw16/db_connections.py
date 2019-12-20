from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base

DB_USER = 'postgres'
DB_PASSWORD = 'postgres'
DB_NAME = 'Car - Brand'
DB_ECHO = True
ENGINE = create_engine(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
    echo=False,
)
if not database_exists(ENGINE.url):
    create_database(ENGINE.url)

Base = declarative_base()
