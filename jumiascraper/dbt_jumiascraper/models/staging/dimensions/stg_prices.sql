WITH stg_prices AS (
    SELECT * FROM {{ source('phones', 'mobile_phones')}}
),

staged AS (
    SELECT
        md5(trim(data_id)) AS data_hash,
        price AS new_price,
        old_price,
        -- ROUND(((old_price - price) / old_price) * 100, 2) AS discount
        {{ discount_calculator('price', 'old_price') }} AS discount
    FROM stg_prices
)

SELECT * FROM staged
