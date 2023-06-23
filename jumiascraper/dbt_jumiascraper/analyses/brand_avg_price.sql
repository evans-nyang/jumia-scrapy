WITH products AS (
    SELECT * FROM {{ ref('fact_products') }}
),

brands AS (
    SELECT * FROM {{ ref('dim_brands') }}
),

aggregated AS (
    SELECT
        brands.brand,
        ROUND(AVG(products.price), 2) AS avg_price
    FROM brands
    LEFT JOIN products
    ON brands.brand_hash = products.brand_hash
    GROUP BY 1
    ORDER BY 2 DESC
)

SELECT * FROM aggregated
