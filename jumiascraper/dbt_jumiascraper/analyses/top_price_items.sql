WITH products AS (
    SELECT * FROM {{ ref('fact_products') }}
),

brands AS (
    SELECT * FROM {{ ref('dim_brands') }}
),

metas AS (
    SELECT
        url_hash,
        specs 
    FROM {{ ref('stg_metas') }}
),

prices AS (
    SELECT
        data_hash,
        discount
    FROM {{ ref('stg_prices') }}
),

pivoted AS (
    SELECT
        *
    FROM products
    JOIN metas using (url_hash)
    JOIN prices using (data_hash)
    JOIN brands using (brand_hash)
),

final AS (
    SELECT
        brand,
        specs,
        price,
        discount,
        item_url
    FROM pivoted
    ORDER BY price DESC
    LIMIT 10
)

SELECT * FROM final
