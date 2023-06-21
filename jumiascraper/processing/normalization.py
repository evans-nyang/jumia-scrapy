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

def normalize_dataset(dataset):
    normalized_data = []
    for key, value in dataset.items():
        normalized_item = {
            'crawled_at': value['crawled_at'],
            'item_url': value['href'],
            'data_id': normalize_dataid(value['data-id']),
            'brand': value['brand'],
            'specs': value['name2'],
            'price': normalize_price(value['price']),
            'old_price': normalize_price(value['old_price']),
            'discount': normalize_discount(value['discount']),
            'votes': normalize_votes(value['votes']),
            'stars': normalize_stars(value['stars']),
            'image_url': value['image_url'],
            'official_store': normalize_official_store(value['official_store'])
        }
        normalized_data.append(normalized_item)
    return normalized_data
