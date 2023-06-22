# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# from sqlalchemy.orm import sessionmaker
# from .models import Items, db_connect, create_items_table


class JumiascraperPipeline:
    def process_item(self, item, spider):
        return item
    #     # Process the item
    #     # ...

    #     # Generate the output file name
    #     file_name = generate_output_file_name(spider.name)

    #     # Write the item to the output file
    #     with open(file_name, 'a') as f:
    #         # Write the item data to the file
    #         # ...
    #         f.write(item['crawled_at'] + '\n')
    #         f.write(item['item_url'] + '\n')
    #         f.write(item['data_id'] + '\n')
    #         f.write(item['brand'] + '\n')
    #         f.write(item['specs'] + '\n')
    #         f.write(item['price'] + '\n')
    #         f.write(item['old_price'] + '\n')
    #         f.write(item['discount'] + '\n')
    #         f.write(item['votes'] + '\n')
    #         f.write(item['stars'] + '\n')
    #         f.write(item['image_url'] + '\n')
    #         f.write(item['official_store'] + '\n')

    #         # Close the file
    #         f.close()

    #     return item
    # def __init__(self):
    #     """
    #     Initializes database connection and sessionmaker
    #     Creates tables
    #     """
    #     try:
    #         print("Connecting to database...")
    #         engine = db_connect()
    #         create_items_table(engine)
    #         self.Session = sessionmaker(bind=engine)
    #         print("\nConnection Successfull!!")
    #     except Exception as err:
    #         print("Encountered an exception during connection!")
    #         raise err

    # def process_item(self, item, spider):
    #     inform = Items()
    #     session = self.Session()
    #     try:
    #         print("Adding items to database")
    #         session.add(inform)
    #         session.commit()

    #     except:
    #         session.rollback()
    #         raise

    #     finally:
    #         session.close()

    #     return item
