WITH products AS (
    SELECT * FROM {{ ref('fact_products') }}
),

brands AS (
    SELECT * FROM {{ ref('dim_brands') }}
),

aggregated AS (
    SELECT
        brands.brand,
        COUNT(products.*) AS total_item_count
    FROM brands
    INNER JOIN products
    ON brands.brand_hash = products.brand_hash
    GROUP BY 1
    ORDER BY 2 DESC
)

SELECT * FROM aggregated
