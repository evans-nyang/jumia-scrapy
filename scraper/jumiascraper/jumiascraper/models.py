import os
from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.engine.base import Engine
# from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import JSONB
from scrapy.utils.project import get_project_settings

# from . import settings

DeclarativeBase = declarative_base()


def db_connect() -> Engine:
    """
    Creates database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("DATABASE_STRING"))
    

def create_items_table(engine: Engine):
    """
    Create the Items table
    """
    DeclarativeBase.metadata.create_all(engine)


class Items(DeclarativeBase):
    """
    Defines the items model
    """
    __tablename__ = os.environ["TABLE_NAME"]

    id = Column(Integer, primary_key=True)
    inform = Column("inform", JSONB)
