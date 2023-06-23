WITH source AS (
    SELECT * FROM {{ source('phones', 'mobile_phones')}}
),

stg_products AS (
    SELECT
        extract(epoch from crawled_at) AS date_id,
        md5(lower(trim(item_url))) AS url_hash,
        lower(trim(item_url)) AS item_url,
        price,
        md5(trim(data_id)) AS data_hash,
        md5(trim(brand)) AS brand_hash,
        md5(CAST(votes AS TEXT)) AS votes_hash,
        crawled_at
    FROM source
    WHERE item_url IS NOT NULL
    AND crawled_at >= (SELECT MAX(DATE(crawled_at)) FROM mobile_phones)
    AND price IS NOT NULL
),

inter_proxy AS (
    SELECT
        stg_products.*,
        {{ dbt_utils.surrogate_key(['date_id', 'item_url']) }} AS dateid_url_hash
    FROM stg_products
),

final AS (
    SELECT
        inter_proxy.*,
        ROW_NUMBER() OVER (PARTITION BY dateid_url_hash ORDER BY crawled_at DESC) AS entry_order
    FROM inter_proxy
)

SELECT * FROM final WHERE entry_order = 1
