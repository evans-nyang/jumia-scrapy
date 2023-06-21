import os
import json
import psycopg2
from dotenv import load_dotenv, dotenv_values
from normalization import normalize_dataset

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

def load_dataset_from_json(file_path):
    with open(file_path, 'r') as file:
        dataset = json.load(file)
    return dataset

# Dataset file is named 'dataset.json' and located in the 'data' directory
file_path = '../dataset/phones.json'

# Load the dataset from the JSON file
dataset = load_dataset_from_json(file_path)
# print(dataset)

        
# Normalize the dataset
# normalized_dataset = normalize_dataset(value)

for index, value in enumerate(dataset):
    if index < 3:
        # print(value)
        normalized_dataset = normalize_dataset(value)

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=os.environ.get('DB_HOST'), 
    port=int(os.environ.get('DB_PORT')), 
    database=os.environ.get('POSTGRES_DB'), 
    user=os.environ.get('POSTGRES_USER'), 
    password=os.environ.get('POSTGRES_PASSWORD'), 
)

# Open a cursor to perform database operations
cur = conn.cursor()

# # Insert the normalized data into the PostgreSQL table
for item in normalized_dataset:
    print(item)
    query = "INSERT INTO mobile_phones (crawled_at, item_url, data_id, brand, specs, price, old_price, discount, votes, stars, image_url, official_store) " \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
        item['crawled_at'],
        item['item_url'],
        item['data_id'],
        item['brand'],
        item['specs'],
        item['price'],
        item['old_price'],
        item['discount'],
        item['votes'],
        item['stars'],
        item['image_url'],
        item['official_store']
    )
    cur.execute(query, values)

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
