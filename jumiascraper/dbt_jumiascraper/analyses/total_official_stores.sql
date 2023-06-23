WITH stores AS (
    SELECT * FROM {{ ref ('stg_metas') }}
),

aggregated AS (
    SELECT
    {% for official_store in ['True'] %}

        SUM(case when status = '{{ official_store }}' then 1 else 0 end) AS total_official_stores {{ ',' if not loop.last }}

    {% endfor %}
    FROM stores
)

SELECT COUNT(*) FROM aggregated WHERE total_official_stores = 1
