{{
    config(
        materialized='incremental',
        unique_key='votes_hash'
    )
}}

WITH stg_reviews AS (
    SELECT * FROM {{ ref("stg_reviews") }}
),

dim_reviews AS (
    SELECT 
        votes_hash, votes, stars
    FROM stg_reviews
    {{ check_incremental('votes_hash') }}
    -- {% if is_incremental() %}

    -- -- this filter will only be applied on an incremental run
    -- WHERE votes_hash NOT IN (SELECT votes_hash FROM {{ this }})

    -- {% endif %}
)

SELECT * FROM dim_reviews
