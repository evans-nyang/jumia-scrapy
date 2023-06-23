WITH stg_brands AS (
    SELECT * FROM {{ source('phones', 'mobile_phones')}}
),

staged AS (
    SELECT
        DISTINCT trim(brand) AS brand,
        md5(trim(brand)) AS brand_hash
    FROM stg_brands

)

SELECT * FROM staged
