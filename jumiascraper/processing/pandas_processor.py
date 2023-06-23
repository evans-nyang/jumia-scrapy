import json
import pandas as pd

def process_data(input_file, output_file):
    with open(input_file, 'r') as file:
        data = json.load(file)
    
    # Extract the 'inform' dictionary from the data 
    inform_data = data['inform'][0]
    
    # Convert the 'inform' dictionary to a DataFrame
    df = pd.DataFrame.from_dict(inform_data, orient='index')
    
    # Clean up the DataFrame
    df['price'] = df['price'].str.replace(r'[^\d.]', '')
    df['old_price'] = df['old_price'].str.replace(r'[^\d.]', '')
    df['discount'] = df['discount'].str.replace('%', '')
    df['votes'] = df['votes'].str.replace('(', '').str.replace(')', '')
    df['stars'] = df['stars'].str.extract(r'(\d\.\d)')
    df['image_url'] = df['image_url'].str.replace('\?[\d]+', '', regex=True)
    
    # Save the normalized data to a new JSON file
    df.to_json(output_file, orient='records')

if __name__ == "__main__":
    process_data('../dataset/extracted/jumiascraper_2023-06-22T00-02-19.json', '../dataset/normalized/jumiascraper_2023-06-22T00-02-19.json')
