SELECT brand, COUNT(*) AS brand_count
FROM {{ ref('dim_brands') }}
GROUP BY 1
