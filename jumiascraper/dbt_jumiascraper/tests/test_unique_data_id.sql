-- This test checks if the "data_id" values are unique

WITH stg_phones AS (
    SELECT * FROM {{ source('public', 'mobile_phones')}}
)

SELECT
    COUNT(*) - COUNT(DISTINCT data_id) AS num_duplicate_data_ids
FROM stg_phones
