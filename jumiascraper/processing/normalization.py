def normalize_url(url):
    # Remove the 'https://www.jumia.co.ke' prefix
    return url.replace('https://www.jumia.co.ke', '').strip()

def normalize_dataid(data_id):
    # Remove the 'data-id' prefix
    # return data_id.replace('data-id', '').strip()
    return data_id

def normalize_price(price):
    try:
        # Remove non-numeric characters and convert to float
        price = price.replace('KSh', '').replace(',', '').strip()
        return float(price)
    except Exception:
        price = 0.0
        return price

def normalize_discount(discount):
    try:
        # Remove '%' character and convert to float
        discount = discount.replace('%', '').strip()
        return float(discount)
    except Exception:
        discount = 0.0
        return discount

def normalize_votes(votes):
    try:
        # Remove parentheses and convert to integer
        votes = votes.replace('(', '').replace(')', '').strip()
        return int(votes)
    except Exception:
        votes = 0
        return votes

def normalize_stars(stars):
    try:
        # Extract the numeric part of the rating
        stars = stars.split(' ')[0].strip()
        return float(stars)
    except Exception:
        stars = 0
        return stars

def normalize_image_url(image_url):
    # Remove the 'https://ke.jumia.is' prefix
    return image_url.replace('https://ke.jumia.is', '').strip()

def normalize_official_store(official_store):
    # Convert the value to True if 'Official Store', else False
    return official_store == 'Official Store'

def clean_dataset(dataset):
    for item in dataset:
        item['item_url'] = normalize_url(item['href'])
        item['data_id'] = normalize_dataid(item['data-id'])
        item['brand'] = item['brand']
        item['specs'] = item['name2']
        item['price'] = normalize_price(item['price'])
        item['old_price'] = normalize_price(item['old_price'])
        item['discount'] = normalize_discount(item['discount'])
        item['votes'] = normalize_votes(item['votes'])
        item['stars'] = normalize_stars(item['stars'])
        item['image_url'] = normalize_image_url(item['image_url'])
        item['official_store'] = normalize_official_store(item['official_store'])

def remove_duplicates(dataset):
    seen = set()
    new_dataset = []
    for item in dataset:
        if item['data_id'] not in seen:
            seen.add(item['data_id'])
            new_dataset.append(item)
        elif item['data_id'] in seen:
            print(f"Duplicate item found: {item['data_id']}")
            dataset.remove(item)
    return new_dataset

def delete_columns(data, columns):
    for item in data:
        for column in columns:
            item.pop(column, None)
    return data

def normalize_dataset(dataset):
    normalized_data = [value for data in dataset for value in data.get('inform', {}).values() if isinstance(value, dict)]
    clean_dataset(normalized_data)
    delete_columns(normalized_data, ['name2', 'href', 'data-id'])
    normalized_data = remove_duplicates(normalized_data)
    return normalized_data
