DROP TABLE IF EXISTS mobile_phones;

CREATE TABLE mobile_phones (
    crawled_at TIMESTAMP,
    item_url TEXT,
    data_id VARCHAR(20) PRIMARY KEY,
    brand VARCHAR(50),
    specs TEXT,
    price DECIMAL(10, 2),
    old_price DECIMAL(10, 2),
    discount DECIMAL(5, 2),
    votes INTEGER,
    stars DECIMAL(3, 1),
    image_url TEXT,
    official_store BOOLEAN
);
