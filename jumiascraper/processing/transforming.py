import os
import psycopg2
from dotenv import load_dotenv
from normalization import normalize_dataset
from file_reader import load_dataset_from_json
from pandas_processor import process_data

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Dataset file is named 'dataset.json' and located in the 'data' directory
file_path = '../dataset/extracted/jumiascraper_2023-06-21T23-49-42.json'

# Load the dataset from the JSON file
dataset = load_dataset_from_json(file_path)

# Normalize the dataset
normalized_dataset = normalize_dataset(dataset)

print(f"Length of normalized dataset is: {len(normalized_dataset)}")  

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host=os.environ.get('POSTGRES_HOST'), 
    port=int(os.environ.get('DB_PORT')), 
    database=os.environ.get('POSTGRES_DB'), 
    user=os.environ.get('POSTGRES_USER'), 
    password=os.environ.get('POSTGRES_PASSWORD'), 
)

# Open a cursor to perform database operations
cur = conn.cursor()
try:
    # # Insert the normalized data into the PostgreSQL table
    for item in normalized_dataset:
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

except Exception as e:
    print(f"Error: {e}")
    conn.rollback()
else:
    print("Data inserted successfully")
    conn.commit()
finally:
    # Close the cursor and connection
    cur.close()
    conn.close()
