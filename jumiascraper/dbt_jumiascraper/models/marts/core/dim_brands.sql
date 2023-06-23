{{
    config(
        materialized='incremental',
        unique_key='brand_hash'
    )
}}

WITH stg_brands AS (
    SELECT * FROM {{ ref("stg_brands") }}
),

dim_brands AS (
    SELECT 
        brand_hash, brand
    FROM stg_brands
    {{ check_incremental('brand_hash') }}
    -- {% if is_incremental() %}

    -- -- this filter will only be applied on an incremental run
    -- WHERE brand_hash NOT IN (SELECT brand_hash FROM {{ this }})

    -- {% endif %}
)

SELECT * FROM dim_brands
