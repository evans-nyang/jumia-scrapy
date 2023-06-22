WITH stg_metas AS (
    SELECT * FROM {{ source('phones', 'mobile_phones')}}
),

staged AS (
    SELECT
        md5(trim(item_url)) AS url_hash,
        lower(trim(item_url)) AS item_link,
        specs,
        image_url,
        official_store
    FROM stg_metas
)

SELECT * FROM staged
