# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

from sqlalchemy.orm import sessionmaker
from .models import Items, db_connect, create_items_table


class JumiascraperPipeline:
    pass
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        try:
            print("Connecting to database...")
            engine = db_connect()
            create_items_table(engine)
            self.Session = sessionmaker(bind=engine)
            print("\nConnection Successfull!!")
        except Exception as err:
            print("Encountered an exception during connection!")
            raise err

    def process_item(self, item, spider):
        inform = Items()
        session = self.Session()
        try:
            print("Adding items to database")
            session.add(inform)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
