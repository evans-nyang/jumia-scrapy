{{
    config(
        materialized='incremental',
        unique_key='dateid_url_hash'
    )
}}

WITH stg_products AS (
    SELECT * FROM {{ ref ('stg_products') }}
),

dim_brands AS (
    SELECT * FROM {{ ref ('dim_brands') }}
),

dim_reviews AS (
    SELECT * FROM {{ ref ('dim_reviews') }}
),

dim_prices AS (
    SELECT * FROM {{ ref ('stg_prices') }}
),

dim_stores AS (
    SELECT * FROM {{ ref ('stg_metas') }}
),

proxy AS (
    SELECT
        *
    FROM stg_products
    INNER JOIN dim_brands using (brand_hash)
    INNER JOIN dim_reviews using (votes_hash)
    INNER JOIN dim_prices using (data_hash)
    INNER JOIN dim_stores using (url_hash)
),

fact_products AS (
    SELECT DISTINCT
        date_id,
        url_hash,
        price,
        data_hash,
        brand_hash,
        votes_hash,
        dateid_url_hash
    FROM proxy
    {{ check_incremental('dateid_url_hash') }}
    -- {% if is_incremental() %}

    -- -- this filter will only be applied on an incremental run
    -- WHERE dateid_url_hash NOT IN (SELECT dateid_url_hash FROM {{ this }}) 

    -- {% endif %}
)

SELECT * FROM fact_products
