WITH products AS (
    SELECT * FROM {{ ref('fact_products') }}
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
),

final AS (
    SELECT
        specs,
        price,
        discount
    FROM pivoted
    WHERE discount > 0
)

SELECT * FROM final
